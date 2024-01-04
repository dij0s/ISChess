import numpy as np
from collections import defaultdict
from collections.abc import Callable

from lib.GameManager.PlayerSequence import PlayerSequence
from lib.AdvancedHeuristic import AdvancedHeuristic
from lib import BetterMoveByPiece
from lib.GameManager.Timer import Timer

class AdvancedBoard:
    __NUMBER_CREATED_BOARDS: int = 0
    
    __BOARD_PIECE_TYPE_INDEX: int = 0
    __BOARD_PIECE_COLOR_INDEX: int = 1
    __BOARD_PIECE_POSITION_X_INDEX: int = 2
    __BOARD_PIECE_POSITION_Y_INDEX: int = 3

    __BOARD_TIME_ALLOWANCE_FACTOR: float = 0.92

    def __init__(self,
                 board: list[list[str]],
                 playerSequence: PlayerSequence,
                 advancedHeuristic: AdvancedHeuristic,
                 timeBudget: float):
        """
        Initializes a AdvancedBoard object given a board: list[list[int]],
        a player sequence: PlayerSequence and a advancedHeuristic: AdvancedHeuristic 
        """
        AdvancedBoard.__NUMBER_CREATED_BOARDS += 1

        AdvancedBoard.__BOARD_STATES_VISITED = 0

        self.board: np.ndarray = np.array(board)
        self.timeBudget = timeBudget
        self.playerSequence: PlayerSequence = playerSequence
        self.computeDepth: Callable[[int], int] = advancedHeuristic.computeDepth
        self.weights: dict[chr, float] = advancedHeuristic.getWeights(self.board)
        self.__piecesByColor: defaultdict[chr, list[str]] = self.__getPiecesByColor()

    def __getPiecesByColor(self) -> defaultdict[chr, list[str]]:
        """
        Returns a dictionnary that maps the pieces
        present on board for each player color and
        stores its position in the following format :
        
        'pieceType''pieceColor''i''j'
        """

        piecesByColor: defaultdict[chr, list[str]] = defaultdict(lambda: [])

        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                if piece != '' and piece != 'X':
                    currentColor: chr = piece[self.__BOARD_PIECE_COLOR_INDEX]

                    pieceIdentifier: str = f"{piece}{i}{j}"

                    piecesByColor[currentColor].append(pieceIdentifier)

        return piecesByColor
   
    def __getTurnNumber(self) -> int:
        """
        Returns the current turn number.
        """
        return (AdvancedBoard.__NUMBER_CREATED_BOARDS * self.playerSequence.numberOfPlayers) - 1
    
    def resetBoardTurnCount() -> None:
        """
        Helper function used to reset the AdvancedBoard class
        static field __NUMBER_CREATED_BOARDS.
        Only needed and used for simulating purposes.
        """
        AdvancedBoard.__NUMBER_CREATED_BOARDS = 0

    def getPiecesByWeight(self, color: chr):
        """
        Yields the pieces on board for argument-given color
        sorted by their respective heuristical value
        """

        yield from self.__piecesByColor[color]
        # yield from sorted(self.__piecesByColor[color], key=lambda piece: self.weights[piece[0]](self.__getTurnNumber()))
        # yield from sorted(self.__piecesByColor[color], key=lambda piece: self.weights[piece[0]](self.__getTurnNumber()), reverse=True)

    def getSize(self) -> tuple[int, int]:
        """
        Returns a tuple describing the size of the board (lines: int, columns: int)
        """

        return len(self.board), len(self.board[1])

    def getBoardCopy(self) -> np.ndarray:
        """
        Returns a copy of the board list, independent of the base object
        """

        return np.copy(self.board)
    
    def isGameOver(self) -> bool:
        """
        Returns True if the board's main color player king still is present.
        The main color is defined by the PlayerSequence.

        Improves pruning when computing a move.
        """

        return f"k{self.playerSequence.ownTeamColor}" not in map(lambda piece: piece[self.__BOARD_PIECE_TYPE_INDEX:self.__BOARD_PIECE_COLOR_INDEX+1], self.__piecesByColor[self.playerSequence.ownTeamColor])

    def computeEvaluation(self) -> float:
        """
        Returns the computed evaluation of the current board
        based on the defined heuristic.
        """

        evaluation: float = 0

        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                if piece != '' and piece != 'XX':
                    # get our color in sequence
                    sign: int = -1 if piece[self.__BOARD_PIECE_COLOR_INDEX] != self.playerSequence.ownTeamColor else 1
                    currentPiece: chr = piece[self.__BOARD_PIECE_TYPE_INDEX]
                    evaluation += sign * self.weights[currentPiece]((i, j))

        return evaluation

    def rotateBoard(self, nbrRot: int = 2) -> np.ndarray:
        """
        Function used to rotate the board for easier opponent simulation.
        The argument nbrRot define how many 90 degrees rotation will be
        performed. (default: 2, 180 degrees)
        """

        return np.rot90(self.board, k=nbrRot, axes=(0, 1))
    
    def computeNextMove(self, isStochastic: bool = False) -> list[tuple[int, int]]:
        """
        This function returns the following move that shall
        be played based on a minimax alpha beta algorithm.
        """

        timer: Timer = Timer()

        def minimaxAlphaBeta(depth: int, alpha: float, beta: float, bestMove: list, isRoot: bool = False) -> float:
            """
            Helper function used to actually compute the next move, recursively.
            """
            
            # check if we shall maximize for
            # given player or minimize
            currentColor: chr = next(self.playerSequence)
            isMaximizing: bool = True if currentColor is self.playerSequence.ownTeamColor else False

            isOvertime: bool = False

            # incase of near time budget reached
            # we shall go back up in the decision tree
            if timer.getElapsed() >= self.timeBudget * self.__BOARD_TIME_ALLOWANCE_FACTOR:
                # print("Overtime -> the ongoing branches are pruned.")
                isOvertime = True
                
                # incase of time budget reach
                # shall return a case that gets
                # pruned by the decision tree
                # depending on the current's node
                # max/min-imizing goal
                return float('-inf') if isMaximizing else float('+inf')
            else:
                # tracks and counts the total
                # recursion calls made in a single
                # move computation
                AdvancedBoard.__BOARD_STATES_VISITED += 1

            if depth == 0 or self.isGameOver():
                return self.computeEvaluation()

            if isMaximizing:
                maxEvaluation: float = float('-inf')

                for piece in self.getPiecesByWeight(currentColor):

                    i, j = int(piece[self.__BOARD_PIECE_POSITION_X_INDEX]), int(piece[self.__BOARD_PIECE_POSITION_Y_INDEX])
                    pieceType: chr = piece[self.__BOARD_PIECE_TYPE_INDEX]

                    for move in BetterMoveByPiece.pieceMovement[pieceType](currentColor, (i, j), self.board):
                        
                        # save position of further move
                        savedPiece = self.board[move[0]][move[1]]

                        self.board[move[0]][move[1]] = self.board[i][j]
                        self.board[i][j] = ""

                        self.__piecesByColor[currentColor].remove(piece)
                        self.__piecesByColor[currentColor].append(f"{piece[0:2]}{move[0]}{move[1]}")

                        currentEvaluation: float = minimaxAlphaBeta(depth - 1, alpha, beta, bestMove)

                        if isOvertime:
                            return float('-inf')

                        # restore position of move
                        self.board[i][j] = self.board[move[0]][move[1]]
                        self.board[move[0]][move[1]] = savedPiece

                        self.__piecesByColor[currentColor].remove(f"{piece[0:2]}{move[0]}{move[1]}")
                        self.__piecesByColor[currentColor].append(piece)

                        # maxEvaluation = max(maxEvaluation, currentEvaluation)
                        if currentEvaluation > maxEvaluation:
                            maxEvaluation = currentEvaluation

                            if isRoot:
                                bestMove.clear()
                                bestMove.append([(i,j), (move[0], move[1])])
                        elif currentEvaluation == maxEvaluation:
                            if isRoot:
                                bestMove.append([(i,j), (move[0], move[1])])

                        alpha: float = max(alpha, currentEvaluation)

                        if beta <= alpha:
                            break

                return maxEvaluation

            else:
                minEvaluation: float = float('inf')

                for piece in self.getPiecesByWeight(currentColor):

                    i, j = int(piece[self.__BOARD_PIECE_POSITION_X_INDEX]), int(piece[self.__BOARD_PIECE_POSITION_Y_INDEX])
                    pieceType: chr = piece[self.__BOARD_PIECE_TYPE_INDEX]

                    for move in BetterMoveByPiece.pieceMovement[pieceType](currentColor, (i, j), self.board):
                        savedPiece = self.board[move[0]][move[1]]

                        self.board[move[0]][move[1]] = self.board[i][j]
                        self.board[i][j] = ""

                        self.__piecesByColor[currentColor].remove(piece)
                        self.__piecesByColor[currentColor].append(f"{piece[0:2]}{move[0]}{move[1]}")

                        currentEvaluation: float = minimaxAlphaBeta(depth - 1, alpha, beta, bestMove)

                        if isOvertime:
                            return float('+inf')

                        # restore position of move
                        self.board[i][j] = self.board[move[0]][move[1]]
                        self.board[move[0]][move[1]] = savedPiece

                        self.__piecesByColor[currentColor].remove(f"{piece[0:2]}{move[0]}{move[1]}")
                        self.__piecesByColor[currentColor].append(piece)

                        minEvaluation = min(minEvaluation, currentEvaluation)
                        beta: float = min(beta, currentEvaluation)

                        if beta <= alpha:
                            break

                return minEvaluation

        depth: int = self.computeDepth()

        bestMoveWrapper: list = []
        minimaxAlphaBeta(depth, float('-inf'), float('+inf'), bestMoveWrapper, True)
        print(f"{AdvancedBoard.__BOARD_STATES_VISITED} states have been evaluated with a depth of {depth}.")
        print(bestMoveWrapper)
        moveIndex: int = np.random.randint(0, len(bestMoveWrapper) - 1) if (len(bestMoveWrapper) != 1 and isStochastic) else -1

        return bestMoveWrapper[moveIndex]