from gamestatus import GameStatus
import math


class Minimax:
    """Class that creates the minimax algorithm."""

    def __init__(self):
        """Class constructor, creates variables."""
        self.gamestatus = GameStatus()
        # depth = 6 at start

    def minimax(self, gamestatus, depth, alpha, beta, maximizing_player: bool):
        """Minimax algorithm."""
        if depth == 0 or gamestatus.is_game_over() is True:
            return  # heuristinen arvo
        if maximizing_player:
            value = -math.inf
            for move in gamestatus.possible_moves:  # list empty right now
                value = max(value, self.minimax(
                    move, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if value >= beta:
                    break
            return value
        else:
            value = math.inf
            for move in gamestatus.possible_moves:  # list empty right now
                value = min(value, self.minimax(
                    move, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if value <= alpha:
                    break
            return value

    def main(self):
        self.minimax(self.gamestatus, 6)

# for testing
if __name__ == "__main__":
    game = Minimax()
    game.main()
