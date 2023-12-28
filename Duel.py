from numpy import array

from lib.GameManager import *
from Bots.BestChessBot import chess_bot as bestChessAI
from Bots.npcChessBot import chess_bot as npcChessAI

class Duel:
    """
    Class used to simulate a duel between
    two bots and finally compute some statistical
    information.
    """

    def __init__(self, boardConfigurationFile: str) -> None:
        self.__loadBoard(boardConfigurationFile)
        
        self.botsAIbyColor: dict = {}
        self.botsAIbyColor['w'] = bestChessAI
        self.botsAIbyColor['b'] = npcChessAI

    def __loadBoard(self, boardConfigurationFile: str) -> None:
        """
        Helper function used to load the board
        and instantiate the further needed objects.
        """

        with open(boardConfigurationFile) as configurationFile:
            rawConfigurationFile: list[str] = list(map(str.rstrip, configurationFile.readlines()))

            self.rawPlayerSequence: str = rawConfigurationFile[0]
            self.playerSequence: PlayerSequence = PlayerSequence(rawConfigurationFile[0])
            self.board: array = array([l.replace('--', '').split(",") for l in rawConfigurationFile[1:]], dtype='O')

    def start(self, numberOfPlays: int, timeBudget: float) -> None:
        """
        Simulates a chess duel with an argument-given
        number of plays and allowed time budget
        for the current game.
        """

        for _ in range(numberOfPlays):
            currentColor: chr = next(self.playerSequence)
            currentAI: function = self.botsAIbyColor[currentColor]
            
            timer: Timer = Timer()

            nextMove: list = currentAI(self.rawPlayerSequence, self.board, timeBudget)
            print(f"This is the move {nextMove}")