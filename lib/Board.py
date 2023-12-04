import numpy as np
from lib.GameManager.PlayerSequence import PlayerSequence
from lib.Heuristic import Heuristic

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
        self.board = np.array(board)
        self.playerSequence = playerSequence
        self.weights = heuristic.getWeights()

    def getTurnNumber(self) -> int:
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

    def computeEvaluation(self):
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

        for row in self.board:
            for piece in row:
                if piece != '' and piece != 'X':
                    sign: int = -1 if piece[self.__BOARD_PIECE_COLOR_INDEX] != 'w' else 1
                    currentPiece: chr = piece[self.__BOARD_PIECE_TYPE_INDEX]
                    evaluation += sign * self.weights[currentPiece](0)

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
    
    def computeNextMove(self):
        # blanc joue
        print(next(self.playerSequence))
        # calculer meilleur move blanc


    
    # definition de l'heuristique ?
    # gestion et calculs du prochain coup
    # prendre pièce avec plus petit coup et
    # calculer coups suivants ?