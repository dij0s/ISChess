import copy
import numpy as np
from lib.GameManager.PlayerSequence import PlayerSequence

class Board:
    def __init__(self, boardIn: list[list[str]], playerSequence: PlayerSequence):
        """Initialize a board as boardIn: list[list[str]]"""

        # maybe, at init, store all the pieces
        # of a given player in a hashmap..
        self.board = np.array(boardIn)
        self.playerSequence = playerSequence

    def getSize(self) -> tuple[int, int]:
        """Returns a tuple describing the size of the board (lines: int, columns: int)"""
        return len(self.board), len(self.board[1])

    def getBoardCopy(self) -> np.ndarray:
        """Returns a copy of the board list, independent of the base object"""
        return np.copy(self.board)

    def computeEval(self):
        print("compute the eval here")

    def rotateBoard(self, nbrRot:int = 2) -> np.ndarray:
        """ Function used to rotate the board for easier opponent simulation.
            The argument nbrRot define how many 90 degrees rotation will be
            performed. (default: 2, 180 degrees)"""
        return np.rot90(self.board, k=nbrRot, axes=(0, 1))
    
    def computeNextMove(self):
        # blanc joue
        print(next(self.playerSequence))
        # calculer meilleur move blanc
        

    
    # definition de l'heuristique ?
    # gestion et calculs du prochain coup
    # prendre pièce avec plus petit coup et
    # calculer coups suivants ?