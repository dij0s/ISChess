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
        """
        Returns the current weights of the
        different chess pieces.
        """

        pass

    @abstractmethod
    def computeDepth() -> int:
        """
        Computes and returns the current depth
        of the chess board based on its pieces
        weights.
        """

        pass