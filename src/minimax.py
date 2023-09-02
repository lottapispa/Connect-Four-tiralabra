import math
import time


class Minimax:
    """Class that creates the minimax algorithm."""

    def __init__(self, gamerack, gamestatus, score):
        """Class constructor, creates variables."""
        self.gamerack = gamerack
        self.gamestatus = gamestatus
        self.score = score
        self.depth = 10
        self.max_time = 0.1

    def minimax(self, rack, depth, alpha, beta, maximizing_player: bool):
        """Minimax algorithm."""
        is_game_over = self.gamestatus.is_game_over(rack)
        if depth == 0 or (time.time() - self.start) > self.max_time or is_game_over is True:
            return self.score.score_for_moves(rack, self.gamerack.ai_color)
        if maximizing_player:
            best_value = -math.inf
            for move in self.gamerack.next_move(rack):
                rack_copy = self.copy_list(rack)
                self.gamerack.insert_piece(
                    rack_copy, move[0], move[1], self.gamerack.ai_color)
                new_value = self.minimax(
                    rack_copy, depth - 1, alpha, beta, False)
                best_value = max(best_value, new_value)
                alpha = max(alpha, best_value)
                if alpha >= beta:
                    break
            return best_value
        else:
            best_value = math.inf
            for move in self.gamerack.next_move(rack):
                rack_copy = self.copy_list(rack)
                self.gamerack.insert_piece(
                    rack_copy, move[0], move[1], self.gamerack.players_color)
                new_value = self.minimax(
                    rack_copy, depth - 1, alpha, beta, True)
                best_value = min(best_value, new_value)
                beta = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_value

    def choose_best_move(self, rack, piece):
        """This function chooses the move that has the best score.
        Returns: best move as list [row, column]."""
        best_score = -math.inf
        best_move = []
        for place in self.gamerack.next_move(rack):
            self.start = time.time()
            rack_copy = self.copy_list(rack)
            self.gamerack.insert_piece(rack_copy, place[0], place[1], piece)
            if self.gamestatus.is_game_over(rack_copy) and self.gamestatus.winner == piece:
                return place
            else:
                if self.opp_next(rack_copy):
                    continue
            score = self.minimax(rack_copy, self.depth, -
                                 math.inf, math.inf, True)
            if score > best_score:
                best_score = score
                best_move = place
        return best_move

    def copy_list(self, rack):
        """Returns: a copy of the list given as a parameter."""
        rack_copy = []
        for row in rack:
            rack_copy.append(row.copy())
        return rack_copy

    def opp_next(self, rack):
        """This function checks if the opponent will win on the next move. Returns: True if opp wins, False if not."""
        for place in self.gamerack.next_move(rack):
            opp_rack_copy = self.copy_list(rack)
            self.gamerack.insert_piece(
                opp_rack_copy, place[0], place[1], self.gamerack.players_color)
            if self.gamestatus.is_game_over(opp_rack_copy) and self.gamestatus.winner == self.gamerack.players_color:
                return True
