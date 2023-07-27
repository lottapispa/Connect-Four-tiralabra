from gamestatus import GameStatus
from maximizer import Maximizer
from minimizer import Minimizer
from commands import COMMANDS

class Minimax:
    """Class that creates the minimax algorithm."""
    def __init__(self):
        """Class constructor, creates variables."""
        self.gamestatus = GameStatus()
        self.maximizer = Maximizer()
        self.minimizer = Minimizer()
        self.commands = COMMANDS

    def algorithm(self, gamestatus, depth, a, b, maximizing_player):
        if depth == 0:
            return gamestatus
