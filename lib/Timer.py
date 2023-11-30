import time

class Timer:
    timeStart = 0

    def __init__(self):
        self.timeStart = 0
    def initTimer(self):
        """ Initialise the timer """
        self.timeStart = time.time()

    def getDelta(self):
        """ returns the delta time since the last initTimer"""
        return time.time() - self.timeStart
