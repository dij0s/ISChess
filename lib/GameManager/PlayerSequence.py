class PlayerSequence(object):
    """
    Class used to ease the players sequence handling.
    The following class is only instantiated once as
    it is a singleton.
    """
    
    __TEAM_STRING_LENGTH: int = 3

    __TEAM_STRING_ID_INDEX: int = 0
    __TEAM_STRING_COLOR_INDEX: int = 1
    __TEAM_STRING_ROTATION_INDEX: int = 2

    def __getTeams(self, sequence: str) -> dict[chr, int]:
        teams: dict[chr, int] = {}
        # complete dictionnary of the
        # teams and corresponding id
        for relativeIndex in range(self.numberOfPlayers):
            absoluteIndex: int = relativeIndex * self.__TEAM_STRING_LENGTH
            # could be improved by avoiding slicing
            currentTeamSequence: str = sequence[absoluteIndex : absoluteIndex + self.numberOfPlayers + 1]
            teams.update({
                currentTeamSequence[self.__TEAM_STRING_COLOR_INDEX]:
                currentTeamSequence[self.__TEAM_STRING_ID_INDEX]
            })

        self.__teams: list[chr] = list(teams.keys())

        return teams
    
    def __getBoardsRotation(self, sequence: str) -> dict[chr, int]:
        boardsRotation: dict[chr, int] = {}
        boardColorRotationMapping = lambda rotationIndex: -(int(rotationIndex) - 2)

        for relativeIndex in range(self.numberOfPlayers):
            absoluteIndex: int = relativeIndex * self.__TEAM_STRING_LENGTH
            # could be improved by avoiding slicing
            currentTeamSequence: str = sequence[absoluteIndex : absoluteIndex + self.numberOfPlayers + 1]
            boardsRotation.update({
                currentTeamSequence[self.__TEAM_STRING_COLOR_INDEX]:
                boardColorRotationMapping(currentTeamSequence[self.__TEAM_STRING_ROTATION_INDEX])
            })

        return boardsRotation

    def __new__(self, sequence: str, *args, **kwargs):
        if not hasattr(self, 'instance'):
            self.instance = super(PlayerSequence, self).__new__(self, *args, **kwargs)
        
        return self.instance
    
    def __init__(self, sequence: str, *args, **kwargs) -> None:
        super().__init__(*args, *kwargs)

        self.numberOfPlayers: int = len(sequence) // self.__TEAM_STRING_LENGTH
        self.rotationPerPlay: int = (360 // self.numberOfPlayers) // 90
        self.teamsId: dict[chr, int] = self.__getTeams(sequence)
        self.teamsBoardRotation: dict[chr, int] = self.__getBoardsRotation(sequence)
        self.ownTeamColor: chr = sequence[self.__TEAM_STRING_COLOR_INDEX]
        self.__teamsIterator = self.__iter__()

    def __iter__(self):
        while 1:
            yield from self.__teams

    def __next__(self) -> chr:
        """
        Returns next team's color in order of play.
        """
        # forgot return keyword
        return next(self.__teamsIterator)