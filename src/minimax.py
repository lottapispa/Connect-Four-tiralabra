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
        self.turn = None #who's turn is it, player 1 or 2

    def minimax(self, gamestatus, depth, a, b, maximizing_player: bool):
        if depth == 0 or gamestatus.is_game_over() is True:
            return  # heuristinen arvo
        
    def choose_move(self):
        pass

    def main(self):
        color = input("Choose color: 'red' or 'yellow'.")
        who_starts = input("Do you want the first move? Type 'yes' or 'no'.")
        if who_starts == "yes":
            self.turn = 1
            print("You are player 1.")
        else:
            self.turn = 2
            print("You are player 2.")
        while self.gamestatus.is_game_over() is False:
            if self.turn == 1:
                move = input("Player 1, make your move")
        #self.minimax()

# for testing
if __name__ == "__main__":
    x = Minimax()
    x.main()
