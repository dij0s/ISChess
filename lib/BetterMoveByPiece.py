def MoveKing(color: chr, pos: tuple[int, int], board: list[list[str]]):
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if not(j == 0 and i == 0) and legalMove(color, [pos[0] + i, pos[1] + j], board):
                yield [pos[0] + i, pos[1] + j]


def MoveQueen(color: chr, pos: tuple[int, int], board: list[list[str]]):
    yield from MoveBishop(color, pos, board)
    yield from MoveRook(color, pos, board)

def MoveRook(color: chr, pos: tuple[int, int], board: list[list[str]]):
    for i in range(0,4):
        # must remove hard-coded values
        # hence maybe pass in a Board
        # class argument on which we can
        # get the size in constant time
        for j in range(1, 8):
            match i:
                case 0:
                    if legalMove(color, [pos[0], pos[1] + j], board):
                        if board[pos[0]][pos[1] + j] == "":
                            yield [pos[0], pos[1] + j]
                        elif board[pos[0]][pos[1] + j][1] != color:
                            yield [pos[0], pos[1] + j]
                            break
                        else: break
                    else: break
                case 1:
                    if legalMove(color, [pos[0], pos[1] - j], board):
                        if board[pos[0]][pos[1] - j] == "":
                            yield [pos[0], pos[1] - j]
                        elif board[pos[0]][pos[1] - j][1] != color:
                            yield [pos[0], pos[1] - j]
                            break
                        else: break
                    else: break
                case 2:
                    if legalMove(color, [pos[0] + j, pos[1]], board):
                        if board[pos[0] + j][pos[1]] == "":
                            yield [pos[0] + j, pos[1]]
                        elif board[pos[0] + j][pos[1]][1] != color:
                            yield [pos[0] + j, pos[1]]
                            break
                        else: break
                    else: break
                case 3:
                    if legalMove(color, [pos[0] - j, pos[1]], board):
                        if board[pos[0] - j][pos[1]] == "":
                            yield [pos[0] - j, pos[1]]
                        elif board[pos[0] - j][pos[1]][1] != color:
                            yield [pos[0] - j, pos[1]]
                            break
                        else: break
                    else: break

def MoveKnight(color: chr, pos: tuple[int, int], board: list[list[str]]):
    moveList = [[2, 1], [2, -1], [-2, 1], [-2, -1]]
    for i in moveList:
        if legalMove(color, [pos[0] + i[0], pos[1] + i[1]], board):
            yield [pos[0] + i[0], pos[1] + i[1]]
        if legalMove(color, [pos[0] + i[1], pos[1] + i[0]], board):
            yield [pos[0] + i[1], pos[1] + i[0]]

def MoveBishop(color: chr, pos: tuple[int, int], board: list[list[str]]):
    for i in range(0, 4):
        for j in range(1, 8):
            match i:
                case 0: # ++
                    if legalMove(color, [pos[0] + j, pos[1] + j], board):
                        if board[pos[0] + j][pos[1] + j] == "":
                            yield [pos[0] + j, pos[1] + j]
                        elif board[pos[0]+ j][pos[1] + j][1] != color:
                            yield [pos[0] + j, pos[1] + j]
                            break
                        else: break
                    else: break
                case 1: # --
                    if legalMove(color, [pos[0] - j, pos[1] - j], board):
                        if board[pos[0] - j][pos[1] - j] == "":
                            yield [pos[0] - j, pos[1] - j]
                        elif board[pos[0] - j][pos[1] - j][1] != color:
                            yield [pos[0] - j, pos[1] - j]
                            break
                        else: break
                    else: break
                case 2: # +-
                    if legalMove(color, [pos[0] + j, pos[1] - j], board):
                        if board[pos[0] + j][pos[1] - j] == "":
                            yield [pos[0] + j, pos[1] - j]
                        elif board[pos[0]+ j][pos[1] - j][1] != color:
                            yield [pos[0] + j, pos[1] - j]
                            break
                        else: break
                    else: break
                case 3: # -+
                    if legalMove(color, [pos[0] - j, pos[1] + j], board):
                        if board[pos[0] - j][pos[1] + j] == "":
                            yield [pos[0] - j, pos[1] + j]
                        elif board[pos[0] - j][pos[1] + j][1] != color:
                            yield [pos[0] - j, pos[1] + j]
                            break
                        else: break
                    else: break

def MovePawn(color: chr, pos: tuple[int, int], board: list[list[str]]):
    if color == "b":        #Color check for temporary tests, rotate board acording to player?
        if legalMove(color, [pos[0] + 1,pos[1]], board):
            if board[pos[0] + 1][pos[1]] == "":
                yield [pos[0] + 1, pos[1]]
        if legalMove(color, [pos[0] + 1,pos[1] + 1], board):
            if board[pos[0] + 1][pos[1] + 1] != color and board[pos[0] + 1][pos[1] + 1] != "":
                yield [pos[0] + 1, pos[1] + 1]
        if legalMove(color, [pos[0] + 1, pos[1] - 1], board):
            if board[pos[0] + 1][pos[1] - 1] != color and board[pos[0] + 1][pos[1] - 1] != "":
                yield [pos[0] + 1, pos[1] - 1]

    if color == "w":
        if legalMove(color, [pos[0] - 1,pos[1]], board):
            if board[pos[0] - 1][pos[1]] == "":
                yield [pos[0] - 1, pos[1]]
        if legalMove(color, [pos[0] - 1,pos[1] + 1], board):
            if board[pos[0] - 1][pos[1] + 1] != color and board[pos[0] - 1][pos[1] + 1] != "":
                yield [pos[0] - 1, pos[1] + 1]
        if legalMove(color, [pos[0] - 1, pos[1] - 1], board):
            if board[pos[0] - 1][pos[1] - 1] != color and board[pos[0] - 1][pos[1] - 1] != "":
                yield [pos[0] - 1, pos[1] - 1]

def legalMove(color: chr, pos: tuple[int, int], board: list[list[str]]):
    if 7 >= pos[0] >= 0 and 7 >= pos[1] >= 0:
        if board[pos[0]][pos[1]] == "":
            return True
        elif board[pos[0]][pos[1]][1] != color:
            return True
        else:
            return False
    else:
        return False