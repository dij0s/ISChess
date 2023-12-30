from numpy import array, rot90
from collections import defaultdict
from collections.abc import Callable

from lib.GameManager import *
from lib.Board import Board

class Duel:
    """
    Class used to simulate a duel between
    two bots and finally compute some statistical
    information.
    """

    def __init__(self, boardConfigurationFile: str, whiteAI: Callable[[str, list[list[str]], float], list[tuple[int, int]]], blackAI: Callable[[str, list[list[str]], float], list[tuple[int, int]]]) -> None:
        self.__loadBoard(boardConfigurationFile)
        
        self.botsAIbyColor: dict = {}
        self.botsAIbyColor['w'] = whiteAI
        self.botsAIbyColor['b'] = blackAI

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

    def __checkForWinner(self) -> str:
        """
        Helper function used to check for
        a potential winner in the current
        board's state.
        A win is defined as the state of the board
        following the king being taken or the board's
        final state which depends on its evaluation.
        """
        
        numberOfPiecesByColor: defaultdict = defaultdict(int)
        hasWhiteKing, hasBlackKing = False, False

        for line in self.board:
            for piece in line:
                if piece != '' and piece != 'XX':
                    numberOfPiecesByColor[piece[1]] += 1

                if piece == 'kw':
                    hasWhiteKing = True
                elif piece == 'kb':
                    hasBlackKing = True

        if hasWhiteKing and hasBlackKing:
            # returns the winner in the sense
            # of the total number of pieces
            # on the current board
            if numberOfPiecesByColor['w'] > numberOfPiecesByColor['b']:
                return 'w-nocheckmate'
            elif numberOfPiecesByColor['b'] > numberOfPiecesByColor['w']:
                return 'b-nocheckmate'
            else:
                return 'draw'
        
        elif not hasWhiteKing:
            return 'b'
        else:
            return 'w'
        
    def simulateSingleGame(self, numberOfPlays: int, timeBudget: float) -> str:
        """
        Simulates a chess duel with an argument-given
        number of plays and allowed time budget
        for the current game.
        Returns the winner of the game.
        """

        for _ in range(numberOfPlays):
            currentColor: chr = next(self.playerSequence)
            currentAI: Callable[[str, list[list[str]], float], list[tuple[int, int]]] = self.botsAIbyColor[currentColor]
            
            nextMove: list = currentAI(self.rawPlayerSequence, self.board, timeBudget)
            oldPositionX, oldPositionY = nextMove[0]
            newPositionX, newPositionY = nextMove[1]

            self.board[newPositionX][newPositionY] = self.board[oldPositionX][oldPositionY]
            self.board[oldPositionX][oldPositionY] = ''

            self.board = rot90(self.board, self.playerSequence.rotationPerPlay)
            self.rawPlayerSequence = f"{self.rawPlayerSequence[3:]}{self.rawPlayerSequence[0:3]}"

            winner: str = self.__checkForWinner()
            
            if winner == 'w' or winner == 'b':
                return winner
            
        return self.__checkForWinner()

    def simulateGames(boardConfigurationFile: str, whiteAI: Callable[[str, list[list[str]], float], list[tuple[int, int]]], blackAI: Callable[[str, list[list[str]], float], list[tuple[int, int]]], numberOfGames: int, numberOfPlays: int, timeBudget: float) -> defaultdict:
        """
        Simulates an argument-given number of games of chess
        with an argument-given number of plays and allowed
        time budget for the current game.
        """

        winStatisticsByColor: defaultdict = defaultdict(int)

        for _ in range(numberOfGames):
            newDuel: Duel = Duel('./Data/maps/default.brd', whiteAI, blackAI)
            winStatisticsByColor[newDuel.simulateSingleGame(numberOfPlays, timeBudget)] += 1

            Board.resetBoardTurnCount()

        return winStatisticsByColor