import numpy as np

from lib.GameManager.PlayerSequence import PlayerSequence
from lib.Heuristic import Heuristic
from lib import BetterMoveByPiece

from collections import defaultdict

class Board:
    __NUMBER_CREATED_BOARDS: int = 0
    
    __BOARD_PIECE_TYPE_INDEX: int = 0
    __BOARD_PIECE_COLOR_INDEX: int = 1

    def __init__(self,
                 board: list[list[str]],
                 playerSequence: PlayerSequence,
                 heuristic: Heuristic):
        """
        Initializes a Board object given a board: list[list[int]],
        a player sequence: PlayerSequence and a heuristic: Heuristic 
        """

        Board.__NUMBER_CREATED_BOARDS += 1
        # maybe, at init, store all the pieces
        # of a given player in a hashmap..
        self.board: np.ndarray = np.array(board)
        self.playerSequence: PlayerSequence = playerSequence
        self.computeDepth = heuristic.computeDepth
        self.weights: dict[chr, float] = heuristic.getWeights()
        self.__piecesByColor: defaultdict[chr, list[str]] = self.__getPiecesByColor()

    def __getPiecesByColor(self) -> defaultdict[chr, list[str]]:
        """
        Returns a dictionnary that maps the pieces
        present on board for each player color and
        stores each piece position in a dict
        """

        piecesByColor: defaultdict[chr, list[int]] = defaultdict(lambda: [])
        piecesPosition: defaultdict[str, tuple(int, int)] = defaultdict(lambda: ())

        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                if piece != '' and piece != 'X':
                    currentColor: chr = piece[self.__BOARD_PIECE_COLOR_INDEX]
                    currentPiece: chr = piece[self.__BOARD_PIECE_TYPE_INDEX]

                    piecesByColor[currentColor].append(currentPiece)
                    piecesPosition[piece] = (i, j)

        self.__piecesPosition: defaultdict[str, tuple(int, int)] = piecesPosition
        return piecesByColor

    
    def getPiecesByWeight(self, color: chr):
        """
        Yields the pieces on board for argument-given color
        sorted by their respective heuristical value
        """

        yield from sorted(self.__piecesByColor[color], key=lambda piece: self.weights[piece](self.__getTurnNumber()))

    def __getTurnNumber(self) -> int:
        """
        Returns the current turn number.
        """

        return (Board.__NUMBER_CREATED_BOARDS * self.playerSequence.numberOfPlayers) - 1

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

    def computeEvaluation(self, boardIn: np.ndarray) -> float:
        """
        Returns the computed evaluation of the current board
        based on the defined heuristic.
        """

        # should we compute the eval during
        # the initialization as a board
        # represents a graph or do we actually
        # modify this board and then compute the
        # new evaluation ?

        evaluation: float = 0

        for row in boardIn:
            for piece in row:
                if piece != '' and piece != 'X':
                    # get our color in sequence
                    sign: int = -1 if piece[self.__BOARD_PIECE_COLOR_INDEX] != self.playerSequence.ownTeamColor else 1
                    currentPiece: chr = piece[self.__BOARD_PIECE_TYPE_INDEX]
                    evaluation += sign * self.weights[currentPiece](self.__getTurnNumber())

        return evaluation

    def rotateBoard(self, nbrRot:int = 2) -> np.ndarray:
        """
        Function used to rotate the board for easier opponent simulation.
        The argument nbrRot define how many 90 degrees rotation will be
        performed. (default: 2, 180 degrees)
        """

        # implement by making use of the fact
        # that we can get the board rotation
        # from the PlayerSequence object

        return np.rot90(self.board, k=nbrRot, axes=(0, 1))
    
    def computeNextMove(self) -> float:
        """
        This function returns the following move that shall
        be played based on a minimax alpha beta algorithm.
        """

        def minimaxAlphaBeta(board: np.ndarray, depth: int, alpha: float, beta: float) -> float:
            """
            Helper function used to actually compute the next move, recursively.
            """
            # check if we shall maximize for given
            # player or actually minimize
            currentColor: chr = next(self.playerSequence)
            print(alpha, beta)
            isMaximizing: bool = True if currentColor is self.playerSequence.ownTeamColor else False
            # shall check for game over too
            # maybe define a function that
            # checks that
            if depth == 0:
                return self.computeEvaluation(board)

            if isMaximizing:
                maxEvaluation: float = float('-inf')

                for pieceType in self.getPiecesByWeight(currentColor):
                    i, j = self.__piecesPosition[f"{pieceType}{currentColor}"]
                   
                    for move in BetterMoveByPiece.pieceMovement[pieceType](currentColor, (i, j), self.board):
                        savedPiece = board[move[0]][move[1]]
                        
                        board[move[0]][move[1]] = board[i][j]
                        board[i][j] = ""

                        currentEvaluation: float = minimaxAlphaBeta(board, depth - 1, alpha, beta)
                        
                        board[i][j] = board[move[0]][move[1]]
                        board[move[0]][move[1]] = savedPiece

                        maxEvaluation = max(maxEvaluation, currentEvaluation)
                        alpha: float = max(alpha, currentEvaluation)
                        
                        if beta <= alpha:
                            break

                return maxEvaluation

            else:
                minEvaluation: float = float('inf')

                for pieceType in self.getPiecesByWeight(currentColor):
                    i, j = self.__piecesPosition[f"{pieceType}{currentColor}"]
                    
                    for move in BetterMoveByPiece.pieceMovement[pieceType](currentColor, (i, j), self.board):
                        savedPiece = board[move[0]][move[1]]

                        board[move[0]][move[1]] = board[i][j]
                        board[i][j] = ""

                        currentEvaluation: float = minimaxAlphaBeta(board, depth - 1, alpha, beta)
                        
                        board[i][j] = board[move[0]][move[1]]
                        board[move[0]][move[1]] = savedPiece

                        minEvaluation = min(minEvaluation, currentEvaluation)
                        beta: float = min(beta, currentEvaluation)
                        
                        if beta <= alpha:
                            break

                return minEvaluation


        depth: int = self.computeDepth(self.__getTurnNumber())
        return minimaxAlphaBeta(self.board, depth, float('-inf'), float('inf'))