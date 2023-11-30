from PyQt6 import QtCore
from Bots.ChessBotList import register_chess_bot
from lib.Timer import Timer

def chess_bot(player_sequence, board, time_budget, **kwargs):

    color = player_sequence[1]
    for x in range(board.shape[0]-1):
        for y in range(board.shape[1]):
            if board[x,y] != "p"+color:
                continue
            if y > 0 and board[x+1,y-1] != '' and board[x+1,y-1][-1] != color:
                return (x,y), (x+1,y-1)
            if y < board.shape[1] - 1 and board[x+1,y+1] != '' and board[x+1,y+1][1] != color:
                return (x,y), (x+1,y+1)
            elif board[x+1,y] == '':
                return (x,y), (x+1,y)

    return (0,0), (0,0)

register_chess_bot("Bogoss Overdose", chess_bot)