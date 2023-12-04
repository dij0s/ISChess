import numpy as np
from .Heuristic import Heuristic

class TimeScalingHeuristic(Heuristic):
    """
    The following heuristic will compute and return the
    pieces associated weights considering a time-scaling
    factor.
    It will also compute the minimax algorithm tree depth
    based on the weights variance.
    """
    # Maybe compute in relation to max number of plays too ?

    def __init__(self):
        self.__WEIGHTS: dict[chr, float] = {
            'p': (lambda turn: 1.0 + np.exp(turn / 8)),
            'r': (lambda _: 5.0),
            'n': (lambda _: 3.0),
            'b': (lambda _: 3.0),
            'q': (lambda turn: 9.0 + np.exp(turn / 6)),
            'k': (lambda _: float('inf'))
        }

    def getWeights(self) -> dict:
        return self.__WEIGHTS
        
    def computeDepth(self, turn: int) -> int:
        # must compute based on variance
        # at given round

        # get values of the weights
        # at the argument given turn
        currentWeights: list[float] = list(map(lambda w: w(turn), self.__WEIGHTS.values()))
        meanWeight: float = sum(currentWeights) / len(currentWeights)

        weightsVariance: float = 0
        for w in currentWeights:
            weightsVariance += np.square(w - weightsVariance)
        weightsVariance = weightsVariance / len(weightsVariance)

        return 1.0