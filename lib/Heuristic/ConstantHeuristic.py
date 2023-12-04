import numpy as np
from .Heuristic import Heuristic

class ConstantHeuristic(Heuristic):
    """
    The following heuristic maps the different pieces
    to a constant value that doesn't scale.
    The depth of the minimax alpha beta tree will be
    constant, too.
    """

    def __init__(self):
        self.__WEIGHTS: dict[chr, float] = {
            'p': (lambda _: 1.0),
            'r': (lambda _: 5.0),
            'n': (lambda _: 3.0),
            'b': (lambda _: 3.0),
            'q': (lambda _: 9.0),
            'k': (lambda _: 1e10)
        }
        self.__BASE_DEPTH_: int = 4

    def getWeights(self) -> dict:
        return self.__WEIGHTS
        
    def computeDepth(self, turn: int) -> int:
        return self.__BASE_DEPTH_