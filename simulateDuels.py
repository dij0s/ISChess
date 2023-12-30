from collections import defaultdict
from collections.abc import Callable

from Duel import Duel
from Bots.BestChessBot import chess_bot as bestChessAI
from Bots.npcChessBot import chess_bot as npcChessAI
from Bots.BaseChessBot import chess_bot as baseChessAI

__NUMBER_OF_GAMES: int = 100
__NUMBER_OF_PLAYS: int = 40
__TIME_BUDGET: float = 0.75

__WHITE_AI: Callable = bestChessAI
__BLACK_AI: Callable = npcChessAI

winStatisticsByColor: defaultdict = Duel.simulateGames('./Data/maps/default.brd', __WHITE_AI, __BLACK_AI, __NUMBER_OF_GAMES, __NUMBER_OF_PLAYS, __TIME_BUDGET)

for teamColor, numberOfWins in winStatisticsByColor.items():
    print(f"Team '{teamColor}' won a total of {numberOfWins} game(s).")

print(f"Results yield from {__NUMBER_OF_GAMES} simulation(s) of {__NUMBER_OF_PLAYS} plays games and a time budget of {__TIME_BUDGET}s per play.")
print(f"{__WHITE_AI.__module__} played white and {__BLACK_AI.__module__} played black.")