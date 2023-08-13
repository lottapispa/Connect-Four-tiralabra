import math

class Minimax:
    """Class that creates the minimax algorithm."""

    def __init__(self, gamerack, gamestatus):
        """Class constructor, creates variables."""
        self.gamerack = gamerack
        self.gamestatus = gamestatus
        self.depth = None #6?

    def minimax(self, rack, depth, alpha, beta, maximizing_player: bool):
        """Minimax algorithm."""
        if depth == 0 or self.gamestatus.is_game_over(rack) is True:
            return self.gamestatus.status
        if maximizing_player:
            value = -math.inf
            for move in self.gamerack.next_move(rack):
                #rack_copy = self.gamerack.rack.copy()
                value = max(value, self.minimax(move, depth - 1, -math.inf, math.inf, False))
                alpha = max(alpha, value)
                if value >= beta:
                    break
            return value
        else:
            value = math.inf
            for move in self.gamerack.next_move(rack):
                value = min(value, self.minimax(move, depth - 1, -math.inf, math.inf, True))
                beta = min(beta, value)
                if value <= alpha:
                    break
            return value
