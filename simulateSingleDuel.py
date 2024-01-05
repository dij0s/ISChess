from collections.abc import Callable

from Duel import Duel

from Bots.BestChessBot import chess_bot as TimeScalingAI
from Bots.npcChessBot import chess_bot as ConstantAI
from Bots.GoodChessBot import chess_bot as FixedDepthTimeScalingAI
from Bots.AdvancedChessBot import chess_bot as PlayOrientedAI

__NUMBER_OF_PLAYS: int = 5
__TIME_BUDGET: float = 0.150

__WHITE_AI: Callable = PlayOrientedAI
__BLACK_AI: Callable = ConstantAI

duel: Duel = Duel('./Data/maps/default.brd', __WHITE_AI, __BLACK_AI)
winningTeam: str = duel.simulateSingleGame(__NUMBER_OF_PLAYS, __TIME_BUDGET, withStatistics=True)

print(f"The team '{winningTeam}' won the game.")