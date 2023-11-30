import copy


class Board:
    board: list[list[str]]
    def __init__(self, boardIn: list[list[str]]):
        """Initialise a board as boardIn: list[list[str]]"""
        self.board = boardIn

    def getSize(self):
        """Returns a Tuple describing the size of the board (lines: int, columns: int)"""
        return len(self.board), len(self.board[1])

    def getBoardCopy(self):
        """Returns a copy of the board list, independent of the base object"""
        return copy.deepcopy(self.board)