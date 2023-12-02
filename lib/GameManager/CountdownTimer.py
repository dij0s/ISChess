import time

class CountdownTimer:
    """
    Class used to ease the time management for our chess bot.
    Will notify the user through a callback as we approach the
    end of the timer.
    """
    
    __TIMER_COUNTDOWN_MARGIN: float = 0.98
    __COUNTDOWN_IS_RUNNING: bool = True

    def __init__(self, countdown: int, callback):
        self.timeStart = time.time()
        
        while self.__COUNTDOWN_IS_RUNNING:
            if time.time() - self.timeStart > self.__TIMER_COUNTDOWN_MARGIN * countdown:
                callback()
                break

    def stop(self) -> None:
        """
        Forcefully stop countdown timer.
        """

        self.__COUNTDOWN_IS_RUNNING = False

    # def start(self):
    #     """ Initialize the timer """
    #     self.timeStart = time.time()

    # def getElapsed(self):
    #     """ returns the elapsed time since the last start"""
    #     return time.time() - self.timeStart
