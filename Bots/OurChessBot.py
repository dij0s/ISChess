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

    playerSequence: PlayerSequence = PlayerSequence(player_sequence)
    heuristic: TimeScalingHeuristic = TimeScalingHeuristic()
   
    currentBoard: Board = Board(board, playerSequence, heuristic)
    print(currentBoard.getTurnNumber())

    return (1,0), (2,0)

register_chess_bot("BOGO$$ OVERDOSE", chess_bot)