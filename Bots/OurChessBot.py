from PyQt6 import QtCore
from Bots.ChessBotList import register_chess_bot

import time

# can resolving import cause
# an extra time ? idk
from lib.GameManager import *
from lib.Board import Board

def chess_bot(player_sequence: str, board: list[list[str]], time_budget, **kwargs):   
    
    def returnInCaseOfNoTimeLeft():
        # could define this function
        # in board which returns
        # the current base evaluated
        # move of all computed
        print("arrived at end")

    # countdownTimer: CountdownTimer = CountdownTimer(time_budget, returnInCaseOfNoTimeLeft)
    timer: Timer = Timer()

    # le seul taff du manager est le fait d'être
    # capable de traiter qui joue contre qui et
    # dans quel ordre
    playerSequence: PlayerSequence = PlayerSequence(player_sequence)
    currentBoard: Board = Board(board, playerSequence)

    print(timer.getElapsed())

    # if we actually compute the best move
    # beforehand, we can stop the countdown
    # timer
    # countdownTimer.stop()

    return (1,0), (2,0)

register_chess_bot("BOGO$$ OVERDOSE", chess_bot)