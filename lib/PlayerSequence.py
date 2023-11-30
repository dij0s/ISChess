class PlayerSequence(object):
    """
    Class used to ease the players sequence handling.
    The following class is only instantiated once as
    it is a singleton.
    """
    
    __TEAM_STRING_LENGTH: int = 3
    __TEAM_STRING_ID_POSITION: int = 0
    __TEAM_STRING_COLOR_POSITION: int = 1

    def __getTeams(self, sequence: str) -> dict:
        teams: dict = {}
        # complete dictionnary of the
        # teams and corresponding id
        for relativeIndex in range(self.numberOfPlayers):
            absoluteIndex: int = relativeIndex * self.__TEAM_STRING_LENGTH
            # could be improved by avoiding slicing
            currentTeamSequence: str = sequence[absoluteIndex : absoluteIndex + self.numberOfPlayers + 1]
            teams.update({
                currentTeamSequence[self.__TEAM_STRING_COLOR_POSITION]:
                currentTeamSequence[self.__TEAM_STRING_ID_POSITION]
            })

        self.__teams: list[chr] = list(teams.keys())

        return teams

    def __new__(self, sequence: str, *args, **kwargs):
        if not hasattr(self, 'instance'):
            self.instance = super(PlayerSequence, self).__new__(self, *args, **kwargs)
        
        return self.instance
    
    def __init__(self, sequence: str, *args, **kwargs) -> None:
        super().__init__(*args, *kwargs)

        self.numberOfPlayers = len(sequence) // self.__TEAM_STRING_LENGTH
        self.teamsId: dict = self.__getTeams(sequence)
        self.__teamsIterator = self.__iter__()

    def __iter__(self):
        while True:
            yield from self.__teams

    def __next__(self) -> chr:
        """
        Returns next team's color in order of play.
        """
        # forgot return keyword
        return next(self.__teamsIterator)