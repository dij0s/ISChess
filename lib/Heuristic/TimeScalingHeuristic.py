import numpy as np
from .Heuristic import Heuristic

class TimeScalingHeuristic(Heuristic):
    """
    The following heuristic will compute and return the
    pieces associated weights considering a time-scaling
    factor.
    It will also compute the minimax algorithm alpha beta
    tree depth based on the weights variance.
    """
    # Maybe compute in relation to max number of plays too ?

    def __init__(self):
        # cannot make use of float('inf)
        # as we can't compute the variance
        # maybe use the sys.maxsize ?

        self.__WEIGHTS: dict[chr, float] = {
            'p': (lambda turn: 1.0 + np.exp(turn / 8)),
            'r': (lambda _: 5.0),
            'n': (lambda _: 3.0),
            'b': (lambda _: 3.0),
            'q': (lambda turn: 9.0 + np.exp(turn / 6)),
            'k': (lambda _: 1e10)
        }

        self.__BASE_DEPTH_: int = 4

    def getWeights(self) -> dict:
        return self.__WEIGHTS
        
    def computeDepth(self, turn: int) -> int:
        # must compute based on variance
        # at given round

        # get values of the weights
        # at the argument given turn
        currentWeights: list[float] = list(map(lambda w: w(turn), self.__WEIGHTS.values()))
        depth: int = self.__BASE_DEPTH_ + round(np.log(2 * np.var(currentWeights)))

        return depth