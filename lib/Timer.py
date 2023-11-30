import time

class Timer:
    """Class used to ease the time management for our chess bot"""
    timeStart = 0

    def __init__(self):
        self.timeStart = 0

    def start(self):
        """ Initialize the timer """
        self.timeStart = time.time()

    def getElapsed(self):
        """ returns the elapsed time since the last start"""
        return time.time() - self.timeStart
