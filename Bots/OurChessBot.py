from PyQt6 import QtCore
from Bots.ChessBotList import register_chess_bot

# can resolving import cause
# an extra time ? idk
from lib.GameManager import *
from lib.Board import Board
from lib.Heuristic.TimeScalingHeuristic import TimeScalingHeuristic
from lib.Heuristic.ConstantHeuristic import ConstantHeuristic

def chess_bot(player_sequence: str, board: list[list[str]], time_budget, **kwargs):   

    timer: Timer = Timer()

    playerSequence: PlayerSequence = PlayerSequence(player_sequence)
    # heuristic: TimeScalingHeuristic = TimeScalingHeuristic()
    heuristic: ConstantHeuristic = ConstantHeuristic()
   
    currentBoard: Board = Board(board, playerSequence, heuristic)
    bestMove: list[tuple[int, int]] = currentBoard.computeNextMove()

    return bestMove

register_chess_bot("BOGO$$ OVERDOSE", chess_bot)