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

    def algorithm(self, gamestatus, depth, a, b, maximizing_player):
        if depth == 0 or gamestatus.game_over() == True:
            return  # heuristinen arvo
        
    def main(self):
        self.algorithm(self.gamestatus, self.depth, self.maximizer)

# for testing
if __name__ == "__main__":
    x = Minimax()
    x.main()