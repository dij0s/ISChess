from Bots.ChessBotList import register_chess_bot

from lib.GameManager import *
from lib.Board import Board
from lib.Heuristic.TimeScalingFixedDepthHeuristic import TimeScalingFixedDepthHeuristic

def chess_bot(player_sequence: str, board: list[list[str]], time_budget: float, **kwargs) -> list[tuple[int, int]]:   
    playerSequence: PlayerSequence = PlayerSequence(player_sequence)
    heuristic: TimeScalingFixedDepthHeuristic = TimeScalingFixedDepthHeuristic()

    currentBoard: Board = Board(board, playerSequence, heuristic, time_budget)
    bestMove: list[tuple[int, int]] = currentBoard.computeNextMove()

    return bestMove

register_chess_bot("Good Chess BOT", chess_bot)