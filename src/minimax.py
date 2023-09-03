import math
import time


class Minimax:
    """Class that creates the minimax algorithm."""

    def __init__(self, gamerack, gamestatus, score):
        """Class constructor, creates variables."""
        self.gamerack = gamerack
        self.gamestatus = gamestatus
        self.score = score
        self.max_time = 0.5

    def minimax(self, rack, depth, alpha, beta, maximizing_player: bool, start):
        """Minimax algorithm. Returns: best move as list [row, column] and its score."""
        is_game_over = self.gamestatus.is_game_over(rack)
        if depth == 0 or (time.time() - start) > self.max_time or is_game_over is True:
            return None, self.score.score_for_moves(rack, self.gamerack.ai_color)
        if maximizing_player:
            best_value = -math.inf
            for move in self.gamerack.next_move(rack):
                rack_copy = self.copy_list(rack)
                self.gamerack.insert_piece(
                    rack_copy, move[0], move[1], self.gamerack.ai_color)
                new_value = self.minimax(
                    rack_copy, depth - 1, alpha, beta, False, start)[1]
                if new_value > best_value:
                    best_value = new_value
                    best_move = move
                alpha = max(alpha, best_value)
                if alpha >= beta:
                    break
            return best_move, best_value
        else:
            best_value = math.inf
            for move in self.gamerack.next_move(rack):
                rack_copy = self.copy_list(rack)
                self.gamerack.insert_piece(
                    rack_copy, move[0], move[1], self.gamerack.players_color)
                new_value = self.minimax(
                    rack_copy, depth - 1, alpha, beta, True, start)[1]
                if new_value < best_value:
                    best_value = new_value
                    best_move = move
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_move, best_value

    def copy_list(self, rack):
        """Returns: a copy of the list given as a parameter."""
        rack_copy = []
        for row in rack:
            rack_copy.append(row.copy())
        return rack_copy
