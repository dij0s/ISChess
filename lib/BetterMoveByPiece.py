import numpy as np
from lib.Board import Board

def MoveKing(color: chr, pos: tuple[int,int], board: np.ndarray):
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if not(j == 0 and i == 0) and legalMove(color, (pos[0] + i, pos[1] + j), board):
                yield [pos[0] + i, pos[1] + j]

def MoveQueen(color: chr, pos: tuple[int, int], board: np.ndarray):
    yield from MoveBishop(color, pos, board)
    yield from MoveRook(color, pos, board)


def MoveRook(color: chr, pos: tuple[int, int],board: np.ndarray):
    for i in range(0,4):
        # must remove hard-coded values
        # hence maybe pass in a Board
        # class argument on which we can
        # get the size in constant time
        for j in range(1, board.shape[0]):
            match i:
                case 0:
                    if legalMove(color, (pos[0], pos[1] + j), board):
                        if board[pos[0]][pos[1] + j] == "":
                            yield [pos[0], pos[1] + j]
                        elif board[pos[0]][pos[1] + j][1] != color:
                            yield [pos[0], pos[1] + j]
                            break
                        else: break
                    else: break
                case 1:
                    if legalMove(color, (pos[0], pos[1] - j), board):
                        if board[pos[0]][pos[1] - j] == "":
                            yield [pos[0], pos[1] - j]
                        elif board[pos[0]][pos[1] - j][1] != color:
                            yield [pos[0], pos[1] - j]
                            break
                        else: break
                    else: break
                case 2:
                    if legalMove(color, (pos[0] + j, pos[1]), board):
                        if board[pos[0] + j][pos[1]] == "":
                            yield [pos[0] + j, pos[1]]
                        elif board[pos[0] + j][pos[1]][1] != color:
                            yield [pos[0] + j, pos[1]]
                            break
                        else: break
                    else: break
                case 3:
                    if legalMove(color, (pos[0] - j, pos[1]), board):
                        if board[pos[0] - j][pos[1]] == "":
                            yield [pos[0] - j, pos[1]]
                        elif board[pos[0] - j][pos[1]][1] != color:
                            yield [pos[0] - j, pos[1]]
                            break
                        else: break
                    else: break


def MoveKnight(color: chr, pos: tuple[int, int], board: np.ndarray):
    moveList: list[list[int]] = [[2, 1], [2, -1], [-2, 1], [-2, -1]]
    for i in moveList:
        if legalMove(color, (pos[0] + i[0], pos[1] + i[1]), board):
            yield [pos[0] + i[0], pos[1] + i[1]]
        if legalMove(color, (pos[0] + i[1], pos[1] + i[0]), board):
            yield [pos[0] + i[1], pos[1] + i[0]]


def MoveBishop(color: chr, pos: tuple[int, int], board: np.ndarray):
    for i in range(0, 4):
        for j in range(1, board.shape[0]):
            match i:
                case 0: # ++
                    if legalMove(color, (pos[0] + j, pos[1] + j), board):
                        if board[pos[0] + j][pos[1] + j] == "":
                            yield [pos[0] + j, pos[1] + j]
                        elif board[pos[0] + j][pos[1] + j][1] != color:
                            yield [pos[0] + j, pos[1] + j]
                            break
                        else: break
                    else: break
                case 1: # --
                    if legalMove(color, (pos[0] - j, pos[1] - j), board):
                        if board[pos[0] - j][pos[1] - j] == "":
                            yield [pos[0] - j, pos[1] - j]
                        elif board[pos[0] - j][pos[1] - j][1] != color:
                            yield [pos[0] - j, pos[1] - j]
                            break
                        else: break
                    else: break
                case 2: # +-
                    if legalMove(color, (pos[0] + j, pos[1] - j), board):
                        if board[pos[0] + j][pos[1] - j] == "":
                            yield [pos[0] + j, pos[1] - j]
                        elif board[pos[0] + j][pos[1] - j][1] != color:
                            yield [pos[0] + j, pos[1] - j]
                            break
                        else: break
                    else: break
                case 3: # -+
                    if legalMove(color, (pos[0] - j, pos[1] + j), board):
                        if board[pos[0] - j][pos[1] + j] == "":
                            yield [pos[0] - j, pos[1] + j]
                        elif board[pos[0] - j][pos[1] + j][1] != color:
                            yield [pos[0] - j, pos[1] + j]
                            break
                        else: break
                    else: break


def MovePawn(color: chr, pos: tuple[int, int], board: np.ndarray):
    if legalMove(color, (pos[0] - 1,pos[1]), board):
        if board[pos[0] - 1][pos[1]] == "":
            yield [pos[0] - 1, pos[1]]
    if legalMove(color, (pos[0] - 1,pos[1] + 1), board):
        if board[pos[0] - 1][pos[1] + 1] != color and board[pos[0] - 1][pos[1] + 1] != "":
            yield [pos[0] - 1, pos[1] + 1]
    if legalMove(color, (pos[0] - 1, pos[1] - 1), board):
        if board[pos[0] - 1][pos[1] - 1] != color and board[pos[0] - 1][pos[1] - 1] != "":
            yield [pos[0] - 1, pos[1] - 1]


def legalMove(color: chr, pos: tuple[int, int], board: np.ndarray) -> bool:
    size: tuple[int, int] = board.shape
    # Change condition to check is case is "X"
    if size[0] > pos[0] >= 0 and size[1] > pos[1] >= 0:
        if board[pos[0]][pos[1]] == "":
            return True
        elif board[pos[0]][pos[1]] == "X":
            return False
        elif board[pos[0]][pos[1]][1] != color:
            return True
        else:
            return False
    else:
        return False
