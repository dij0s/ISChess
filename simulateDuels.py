from collections import defaultdict

from Duel import Duel
from Bots.BestChessBot import chess_bot as bestChessAI
from Bots.npcChessBot import chess_bot as npcChessAI
from Bots.BaseChessBot import chess_bot as llChessAI

winStatisticsByColor: defaultdict = Duel.simulateGames('./Data/maps/default.brd', bestChessAI, bestChessAI, 10, 40, 0.125)

for teamColor, numberOfWins in winStatisticsByColor.items():
    print(f"Team '{teamColor}' won a total of {numberOfWins} game(s).")