from Bots.ChessBotList import register_chess_bot

from lib.GameManager import *
from lib.AdvancedBoard import AdvancedBoard
from lib.AdvancedHeuristic.PlayOrientedHeuristic import PlayOrientedHeuristic

def chess_bot(player_sequence: str, board: list[list[str]], time_budget: float, **kwargs) -> list[tuple[int, int]]:   
    playerSequence: PlayerSequence = PlayerSequence(player_sequence)
    advancedHeuristic: PlayOrientedHeuristic = PlayOrientedHeuristic()

    currentBoard: AdvancedBoard = AdvancedBoard(board, playerSequence, advancedHeuristic, time_budget)
    bestMove: list[tuple[int, int]] = currentBoard.computeNextMove()

    return bestMove

register_chess_bot("Play-oriented bot", chess_bot)