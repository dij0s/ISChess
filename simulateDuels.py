from collections import defaultdict

from Duel import Duel

winStatisticsByColor: defaultdict = Duel.simulateGames('./Data/maps/default.brd', 1, 40, 0.125)

for teamColor, numberOfWins in winStatisticsByColor.items():
    print(f"Team '{teamColor}' won a total of {numberOfWins} game(s).")