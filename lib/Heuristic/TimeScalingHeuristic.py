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
        self.__WEIGHTS: dict[chr, float] = {
            'p': (lambda turn: 1.0 * np.exp(turn / 7.5)),
            'r': (lambda _: 5.0),
            'n': (lambda _: 3.0),
            'b': (lambda _: 3.0),
            'q': (lambda turn: 9.0 * np.exp(turn / 6)),
            'k': (lambda _: 1e3)
        }

        self.__BASE_DEPTH_: int = 2
        self.__BASE_STANDARD_DEVIATION: float = np.std(list(map(lambda w: w(0), self.__WEIGHTS.values())))

    def getWeights(self) -> dict:
        return self.__WEIGHTS
        
    def computeDepth(self, turn: int) -> int:
        # must compute based on standard
        # deviation at any given turn

        # get values of the weights
        # at the argument given turn
        currentWeights: list[float] = list(map(lambda w: w(turn), self.__WEIGHTS.values()))

        depth: int = self.__BASE_DEPTH_ + round(np.log(np.std(currentWeights) / self.__BASE_STANDARD_DEVIATION))
        # depth: int = self.__BASE_DEPTH_
        return depth