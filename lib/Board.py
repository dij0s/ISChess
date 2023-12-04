import copy

from lib.GameManager.PlayerSequence import PlayerSequence

class Board:

    
    def __init__(self, boardIn: list[list[str]], playerSequence: PlayerSequence):
        """Initialize a board as boardIn: list[list[str]]"""

        # maybe, at init, store all the pieces
        # of a given player in a hashmap..
        self.board = boardIn
        self.playerSequence = playerSequence

    def getSize(self) -> tuple[int, int]:
        """Returns a tuple describing the size of the board (lines: int, columns: int)"""
        return len(self.board), len(self.board[1])

    def getBoardCopy(self) -> list[list[str]]:
        """Returns a copy of the board list, independent of the base object"""
        return copy.deepcopy(self.board)
    
    def computeNextMove(self):
        # blanc joue
        print(next(self.playerSequence))
        # calculer meilleur move blanc


    
    # definition de l'heuristique ?
    # gestion et calculs du prochain coup
    # prendre pièce avec plus petit coup et
    # calculer coups suivants ?