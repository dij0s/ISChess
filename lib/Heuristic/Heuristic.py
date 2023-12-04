from abc import abstractmethod

class Heuristic(object):
    """
    Parent class used to define heuristics.
    Its childs are only instantiated once as it
    is a singleton.
    """

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Heuristic, self).__new__(self)

        return self.instance

    @abstractmethod
    def getWeights() -> dict[chr, float]:
        pass

    @abstractmethod
    def computeDepth() -> int:
        pass