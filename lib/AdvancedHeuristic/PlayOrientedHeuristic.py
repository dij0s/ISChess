import numpy as np

from .AdvancedHeuristic import AdvancedHeuristic

class PlayOrientedHeuristic(AdvancedHeuristic):
    """
    The following heuristic will compute and return the
    pieces associated weights considering a play-oriented
    factor (through the board's mass center).
    It will also compute the minimax algorithm alpha beta
    tree depth based on the weights standard deviation.
    """

    def __init__(self):
        self.__WEIGHTS: dict[chr, float] = {
            'p': (lambda piecePosition: self.__computeCenterMassProximity(piecePosition, 1.0)),
            'r': (lambda piecePosition: self.__computeCenterMassProximity(piecePosition, 5.0)),
            'n': (lambda piecePosition: self.__computeCenterMassProximity(piecePosition, 3.0)),
            'b': (lambda piecePosition: self.__computeCenterMassProximity(piecePosition, 3.0)),
            'q': (lambda piecePosition: self.__computeCenterMassProximity(piecePosition, 9.0)),
            'k': (lambda piecePosition: self.__computeCenterMassProximity(piecePosition, 1e3))
        }

        self.__BASE_DEPTH_: int = 3

    def __computeCenterMass(self, board: np.array) -> tuple[float, float]:
        validPositionsX: list[float] = []
        validPositionsY: list[float] = []

        for i, row in enumerate(board):
            for j, piece in enumerate(row):
                if piece != '' and piece != 'X':
                    validPositionsX.append(i)
                    validPositionsY.append(j)

        centerMassX: float = sum(validPositionsX) / len(validPositionsX)
        centerMassY: float = sum(validPositionsY) / len(validPositionsY)

        return (centerMassX, centerMassY)
    
    def __computeCenterMassProximity(self, piecePosition: tuple[int, int], defaultWeight: float) -> float:
        euclidianDistance: float = np.sqrt((piecePosition[0] - self.__CENTER_MASS[0])**2 + (piecePosition[1] - self.__CENTER_MASS[1])**2)
        proximityFactor: float = (5 / np.exp(euclidianDistance)) + 1

        return defaultWeight * proximityFactor

    def getWeights(self, board: np.array) -> dict:
        self.__CENTER_MASS: tuple[float, float] = self.__computeCenterMass(board)
        return self.__WEIGHTS
        
    def computeDepth(self) -> int:
        return self.__BASE_DEPTH_