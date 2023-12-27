from PyQt6 import QtCore
from Bots.ChessBotList import register_chess_bot

from lib.GameManager import *
from lib.Board import Board
from lib.Heuristic.TimeScalingHeuristic import TimeScalingHeuristic

def chess_bot(player_sequence: str, board: list[list[str]], time_budget, **kwargs):   
    playerSequence: PlayerSequence = PlayerSequence(player_sequence)
    heuristic: TimeScalingHeuristic = TimeScalingHeuristic()
   
    currentBoard: Board = Board(board, playerSequence, heuristic, time_budget)
    bestMove: list[tuple[int, int]] = currentBoard.computeNextMove()

    return bestMove

register_chess_bot("BOGO$$ OVERDOSE", chess_bot)