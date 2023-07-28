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
        self.depth = 6

    def minimax(self, gamestatus, depth, a, b, maximizing_player: bool):
        if depth == 0 or gamestatus.is_game_over() is True:
            return  # heuristinen arvo
        
    def choose_move(self):
        pass

    def main(self):
        self.minimax()

# for testing
if __name__ == "__main__":
    x = Minimax()
    x.main()
