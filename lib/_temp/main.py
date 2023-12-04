# Quelques tests pour le projet ISChess
# Algorithmique et structures de données
import copy
import random
import time

import MoveByPiece
from lib.Board import Board
from lib.GameManager.PlayerSequence import PlayerSequence
from lib import BetterMoveByPiece

# Dictionnaire contenant les valeurs des pièces
piecesWeight = {
    'p' : 1,
    'r' : 5,
    'n' : 3,
    'b' : 3,
    'q' : 9,
    'k' : 999
}

#Représentation du plateau d'échecs
board = [["rb", "nb", "bb", "qb", "kb", "bb", "nb", "rb"],
         ["pb", "pb", "pb", "pb", "pb", "pb", "pb", "pb"],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["pw", "pw", "pw", "pw", "pw", "pw", "pw", "pw"],
         ["rw", "nw", "bw", "qw", "kw", "bw", "nw", "rw"]]

# Evaluation simple de la position du plateau.
# Pièce adverse: retire des points, notre pièce ajoute des points
def evalPos(board_in):
    score = 0
    for i in board_in:
        for j in i:
            if j != "":
                if j[1] == 'b':
                    score = score - piecesWeight[j[0]]
                elif j[1] == 'w':
                    score = score + piecesWeight[j[0]]
    return score

# Fonction retournant toutes les positions suivantes possible pour une pièce.
# Prends en paramètre la pièce selon le format de la board ainsi que sa pos
def moves(piece, initPos):
    if piece != "":
        match piece[0]:
            case "r":
                return MoveByPiece.MoveRook(piece[1], initPos, board)
            case "n":
                return MoveByPiece.MoveKnight(piece[1], initPos, board)
            case "b":
                return MoveByPiece.MoveBishop(piece[1], initPos, board)
            case "q":
                return MoveByPiece.MoveQueen(piece[1], initPos, board)
            case "k":
                return MoveByPiece.MoveKing(piece[1], initPos, board)
            case "p":
                return MoveByPiece.MovePawn(piece[1], initPos, board)
            case _:
                print("what the hell is this piece, I don't know it")
    else:
        print("found nothing...")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    newBoard = Board(board, PlayerSequence("0w01b2"))

    newBoard.rotateBoard()
    print(newBoard.board.shape)

    '''everyMoveEver = []
    turn = "b"

    t1 = time.time()
    for k in range(0, 1000):
        random.seed()
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] != "" and moves(board[i][j], [i, j]) != []:
                    if board[i][j][1] == turn:
                        everyMoveEver.append([[i, j], moves(board[i][j], [i, j])])
        if turn == "b":
            turn = "w"
        else:
            turn = "b"

        try:
            bestBoard = copy.deepcopy(board)
            prevScore = 0
            tempBoard = []
            for i in range(0,20):
                tempBoard = copy.deepcopy(board)
                pieceToMove = random.randint(0, len(everyMoveEver)-1)
                moveToMake = random.randint(0, len(everyMoveEver[pieceToMove][1])-1)
                thePiece = tempBoard[everyMoveEver[pieceToMove][0][0]][everyMoveEver[pieceToMove][0][1]]
                tempBoard[everyMoveEver[pieceToMove][0][0]][everyMoveEver[pieceToMove][0][1]] = ""
                tempBoard[everyMoveEver[pieceToMove][1][moveToMake][0]][everyMoveEver[pieceToMove][1][moveToMake][1]] = thePiece
                if (prevScore <= evalPos(tempBoard) and turn == "b") or (prevScore >= evalPos(tempBoard) and turn == "w"):
                    prevScore = evalPos(tempBoard)
                    bestBoard = copy.deepcopy(tempBoard)
            board = copy.deepcopy(bestBoard)
            everyMoveEver = []

        except:
            print("Ended after " + str(k) + " turns, " + turn + " wins!")
            break

    for i in board:
        print(i)

    print("Evaluation of the board: " + str(evalPos(board)))
    print(time.time()-t1) # checks how long it takes. 1000 iter = 0.082s
                          # 500 iter = 0.050s
                          # 250 iter = 0.041s     Plus on avance, moins il y a de pièces, plus chaque tour est rapide
                          # 20  iter = 0.004s
'''

#Rotation du plateau ou argument pour donner la direction?
