from PyQt6 import QtCore
from Bots.ChessBotList import register_chess_bot
from lib.Timer import Timer

from lib.PlayerSequence import PlayerSequence

def chess_bot(player_sequence: str, board: list[list[str]], time_budget, **kwargs):
    # le seul taff du manager est le fait d'être
    # capable de traiter qui joue contre qui et
    # dans quel ordre
    playerManager: PlayerSequence = PlayerSequence(player_sequence)
    # can do some pretty cool things
    print(next(playerManager))
    print(next(playerManager))
    print(next(playerManager))

    return (1,0), (2,0)

register_chess_bot("Bogoss Overdose", chess_bot)