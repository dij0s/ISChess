import numpy as np
from .Heuristic import Heuristic

class TimeScalingFixedDepthHeuristic(Heuristic):
    """
    The following heuristic will compute and return the
    pieces associated weights considering a time-scaling
    factor.
    """

    def __init__(self):
        self.__WEIGHTS: dict[chr, float] = {
            'p': (lambda turn: 1.0 * np.exp(turn / 45)),
            'r': (lambda _: 5.0),
            'n': (lambda _: 3.0),
            'b': (lambda _: 3.0),
            'q': (lambda turn: 9.0 * np.exp(turn / 50)),
            'k': (lambda _: 1e3)
        }

        self.__BASE_DEPTH_: int = 4

    def getWeights(self) -> dict:
        return self.__WEIGHTS
        
    def computeDepth(self, turn: int) -> int:
        return self.__BASE_DEPTH_