from abc import abstractmethod

class Heuristic:

    @abstractmethod
    def getWeights() -> dict:
        pass

    @abstractmethod
    def computeDepth() -> int:
        pass