from PyQt6 import QtCore
from Bots.ChessBotList import register_chess_bot

import time

# can resolving import cause
# an extra time ? idk
from lib.GameManager import *
from lib.Board import Board
from lib.Heuristic.TimeScalingHeuristic import TimeScalingHeuristic

def chess_bot(player_sequence: str, board: list[list[str]], time_budget, **kwargs):   

    timer: Timer = Timer()

    # le seul taff du manager est le fait d'être
    # capable de traiter qui joue contre qui et
    # dans quel ordre
    playerSequence: PlayerSequence = PlayerSequence(player_sequence)
    currentBoard: Board = Board(board, playerSequence)

    heuristic: TimeScalingHeuristic = TimeScalingHeuristic()
    print(heuristic.getWeights(0))

    print(timer.getElapsed())

    return (1,0), (2,0)

register_chess_bot("BOGO$$ OVERDOSE", chess_bot)