def MoveKing(color, pos, board):
    moves = []
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if not(j == 0 and i == 0) and legalMove(color, [pos[0] + i, pos[1] + j], board):
                newPos = [pos[0] + i, pos[1] + j]
                moves.append(newPos)
    return moves


def MoveQueen(color, pos, board):
    moves = []
    for i in MoveBishop(color, pos, board):
        moves.append(i)
    for i in MoveRook(color, pos, board):
        moves.append(i)
    return moves

def MoveRook(color, pos, board):
    moves = []
    for i in range(0,4):
        for j in range(1, 8):
            match i:
                case 0:
                    if legalMove(color, [pos[0], pos[1] + j], board):
                        if board[pos[0]][pos[1] + j] == "":
                            moves.append([pos[0], pos[1] + j])
                        elif board[pos[0]][pos[1] + j][1] != color:
                            moves.append([pos[0], pos[1] + j])
                            break
                        else: break
                    else: break
                case 1:
                    if legalMove(color, [pos[0], pos[1] - j], board):
                        if board[pos[0]][pos[1] - j] == "":
                            moves.append([pos[0], pos[1] - j])
                        elif board[pos[0]][pos[1] - j][1] != color:
                            moves.append([pos[0], pos[1] - j])
                            break
                        else: break
                    else: break
                case 2:
                    if legalMove(color, [pos[0] + j, pos[1]], board):
                        if board[pos[0] + j][pos[1]] == "":
                            moves.append([pos[0] + j, pos[1]])
                        elif board[pos[0] + j][pos[1]][1] != color:
                            moves.append([pos[0] + j, pos[1]])
                            break
                        else: break
                    else: break
                case 3:
                    if legalMove(color, [pos[0] - j, pos[1]], board):
                        if board[pos[0] - j][pos[1]] == "":
                            moves.append([pos[0] - j, pos[1]])
                        elif board[pos[0] - j][pos[1]][1] != color:
                            moves.append([pos[0] - j, pos[1]])
                            break
                        else: break
                    else: break

    return moves

def MoveKnight(color, pos, board):
    moves = []
    moveList = [[2, 1], [2, -1], [-2, 1], [-2, -1]]
    for i in moveList:
        if legalMove(color, [pos[0] + i[0], pos[1] + i[1]], board):
            moves.append([pos[0] + i[0], pos[1] + i[1]])
        if legalMove(color, [pos[0] + i[1], pos[1] + i[0]], board):
            moves.append([pos[0] + i[1], pos[1] + i[0]])
    return moves


def MoveBishop(color, pos, board):
    moves = []
    for i in range(0, 4):
        for j in range(1, 8):
            match i:
                case 0: # ++
                    if legalMove(color, [pos[0] + j, pos[1] + j], board):
                        if board[pos[0] + j][pos[1] + j] == "":
                            moves.append([pos[0] + j, pos[1] + j])
                        elif board[pos[0]+ j][pos[1] + j][1] != color:
                            moves.append([pos[0] + j, pos[1] + j])
                            break
                        else: break
                    else: break
                case 1: # --
                    if legalMove(color, [pos[0] - j, pos[1] - j], board):
                        if board[pos[0] - j][pos[1] - j] == "":
                            moves.append([pos[0] - j, pos[1] - j])
                        elif board[pos[0] - j][pos[1] - j][1] != color:
                            moves.append([pos[0] - j, pos[1] - j])
                            break
                        else: break
                    else: break
                case 2: # +-
                    if legalMove(color, [pos[0] + j, pos[1] - j], board):
                        if board[pos[0] + j][pos[1] - j] == "":
                            moves.append([pos[0] + j, pos[1] - j])
                        elif board[pos[0]+ j][pos[1] - j][1] != color:
                            moves.append([pos[0] + j, pos[1] - j])
                            break
                        else: break
                    else: break
                case 3: # -+
                    if legalMove(color, [pos[0] - j, pos[1] + j], board):
                        if board[pos[0] - j][pos[1] + j] == "":
                            moves.append([pos[0] - j, pos[1] + j])
                        elif board[pos[0] - j][pos[1] + j][1] != color:
                            moves.append([pos[0] - j, pos[1] + j])
                            break
                        else: break
                    else: break

    return moves

def MovePawn(color, pos, board):
    moves = []
    if color == "b":        #Color check for temporary tests, rotate board acording to player?
        if legalMove(color, [pos[0] + 1,pos[1]], board):
            if board[pos[0] + 1][pos[1]] == "":
                moves.append([pos[0] + 1, pos[1]])
        if legalMove(color, [pos[0] + 1,pos[1] + 1], board):
            if board[pos[0] + 1][pos[1] + 1] != color and board[pos[0] + 1][pos[1] + 1] != "":
                moves.append([pos[0] + 1, pos[1] + 1])
        if legalMove(color, [pos[0] + 1, pos[1] - 1], board):
            if board[pos[0] + 1][pos[1] - 1] != color and board[pos[0] + 1][pos[1] - 1] != "":
                moves.append([pos[0] + 1, pos[1] - 1])

    if color == "w":
        if legalMove(color, [pos[0] - 1,pos[1]], board):
            if board[pos[0] - 1][pos[1]] == "":
                moves.append([pos[0] - 1, pos[1]])
        if legalMove(color, [pos[0] - 1,pos[1] + 1], board):
            if board[pos[0] - 1][pos[1] + 1] != color and board[pos[0] - 1][pos[1] + 1] != "":
                moves.append([pos[0] - 1, pos[1] + 1])
        if legalMove(color, [pos[0] - 1, pos[1] - 1], board):
            if board[pos[0] - 1][pos[1] - 1] != color and board[pos[0] - 1][pos[1] - 1] != "":
                moves.append([pos[0] - 1, pos[1] - 1])
    return moves


def legalMove(color, pos, board):
    if 7 >= pos[0] >= 0 and 7 >= pos[1] >= 0:
        if board[pos[0]][pos[1]] == "":
            return True
        elif board[pos[0]][pos[1]][1] != color:
            return True
        else:
            return False
    else:
        return False