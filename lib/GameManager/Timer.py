import time

class Timer:
    """Class used to ease the time management for our chess bot"""

    def __init__(self):
        """ Initializes and starts the timer."""
        self.timeStart = time.time()

    # def start(self):
    #     """ Initialize the timer """
    #     self.timeStart = time.time()

    def getElapsed(self) -> float:
        """ Returns the elapsed time since the last start."""
        return time.time() - self.timeStart