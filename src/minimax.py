import math

class Minimax:
    """Class that creates the minimax algorithm."""

    def __init__(self, gamerack, gamestatus):
        """Class constructor, creates variables."""
        self.gamerack = gamerack
        self.gamestatus = gamestatus

    def minimax(self, rack, depth, alpha, beta, maximizing_player: bool):
        """Minimax algorithm."""
        if depth == 0 or self.gamestatus.is_game_over(rack) is True:
            return self.gamestatus.status
        if maximizing_player:
            value = -math.inf
            for move in self.gamerack.next_move(rack):
                rack_copy = self.gamerack.rack.copy()
                self.gamerack.insert_piece(
                    rack_copy, move[0], move[1], self.gamerack.ai_color)
                new_value = self.minimax(
                    rack_copy, depth - 1, -math.inf, math.inf, False)
                if new_value >= value:
                    value = new_value
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return move, value
        else:
            value = math.inf
            for move in self.gamerack.next_move(rack):
                rack_copy = self.gamerack.rack.copy()
                self.gamerack.insert_piece(
                    rack_copy, move[0], move[1], self.gamerack.player_color)
                new_value = self.minimax(
                    rack_copy, depth - 1, -math.inf, math.inf, True)
                if new_value < value:
                    value = new_value
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return move, value
