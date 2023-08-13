from gamestatus import GameStatus
from gamerack import GameRack
import math


class Minimax:
    """Class that creates the minimax algorithm."""

    def __init__(self):
        """Class constructor, creates variables."""
        self.gamestatus = GameStatus()
        self.gamerack = GameRack()
        #depth = 6?

    def minimax(self, gamestatus, depth, alpha, beta, maximizing_player: bool):
        """Minimax algorithm."""
        if depth == 0 or gamestatus.is_game_over() is True:
            return self.gamestatus.status # heuristinen arvo
        if maximizing_player:
            value = -math.inf
            for move in gamestatus.gamerack.next_move():
                value = max(value, self.minimax(
                    move, depth - 1, -math.inf, math.inf, False))
                alpha = max(alpha, value)
                if value >= beta:
                    break
            return value
        else:
            value = math.inf
            for move in gamestatus.gamerack.next_move():
                value = min(value, self.minimax(
                    move, depth - 1, -math.inf, math.inf, True))
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
