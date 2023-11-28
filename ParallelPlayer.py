

from PyQt6 import QtCore

#
#   Thread wrapper
#
class ParallelTurn(QtCore.QThread):
    def __init__(self, AI, player_sequence, board, time_budget):
        super().__init__()

        self.AI = AI
        self.board = board
        self.player_sequence = player_sequence
        self.time_budget = time_budget

        self.team = int(player_sequence[0])
        self.color = player_sequence[1]
        self.board_orientation = int(player_sequence[2])

        self.next_move = ((0,0), (0,0))

    def run(self):
        self.next_move = self.AI(self.player_sequence, self.board, self.time_budget)