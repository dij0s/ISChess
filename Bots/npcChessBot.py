from PyQt6 import QtCore
from Bots.ChessBotList import register_chess_bot

from lib.GameManager import *
from lib.Board import Board
from lib.Heuristic.ConstantHeuristic import ConstantHeuristic

def chess_bot(player_sequence: str, board: list[list[str]], time_budget, **kwargs):   
    playerSequence: PlayerSequence = PlayerSequence(player_sequence)
    heuristic: ConstantHeuristic = ConstantHeuristic()
   
    currentBoard: Board = Board(board, playerSequence, heuristic, time_budget)
    bestMove: list[tuple[int, int]] = currentBoard.computeNextMove(True)

    return bestMove

register_chess_bot("NPC bot", chess_bot)