from collections.abc import Callable

from Duel import Duel

from Bots.BestChessBot import chess_bot as TimeScalingAI
from Bots.npcChessBot import chess_bot as ConstantAI
from Bots.GoodChessBot import chess_bot as FixedDepthTimeScalingAI
from Bots.AdvancedChessBot import chess_bot as PlayOrientedAI
from Bots.BaseChessBot import chess_bot as PawnMoverAI

__NUMBER_OF_PLAYS: int = 70
__TIME_BUDGET: float = 0.750

__WHITE_AI: Callable = TimeScalingAI
__BLACK_AI: Callable = TimeScalingAI

duel: Duel = Duel('./Data/maps/default.brd', __WHITE_AI, __BLACK_AI)
winningTeam: str = duel.simulateSingleGame(__NUMBER_OF_PLAYS, __TIME_BUDGET, withStatistics=True)

print(f"The team '{winningTeam}' won the game.")