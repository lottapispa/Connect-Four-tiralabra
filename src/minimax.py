import math

class Minimax:
    """Class that creates the minimax algorithm."""

    def __init__(self, gamerack, gamestatus, score):
        """Class constructor, creates variables."""
        self.gamerack = gamerack
        self.gamestatus = gamestatus
        self.score = score

    def minimax(self, rack, depth, alpha, beta, maximizing_player: bool):
        """Minimax algorithm."""
        if depth == 0 or self.gamestatus.is_game_over(rack) is True:
            return self.gamestatus.status, self.score.score_for_moves(rack, self.gamerack.ai_color), self.score.score_for_moves(rack, self.gamerack.players_color)
        if maximizing_player:
            value = -math.inf
            for move in self.gamerack.next_move(rack):
                rack_copy = self.gamerack.rack.copy()
                self.gamerack.insert_piece(
                    rack_copy, move[0], move[1], self.gamerack.ai_color)
                new_value = self.minimax(
                    rack_copy, depth - 1, -math.inf, math.inf, False)
                value = max(value, new_value)
                alpha = max(alpha, new_value)
                if alpha >= beta:
                    break
            return value
        else:
            value = math.inf
            for move in self.gamerack.next_move(rack):
                rack_copy = self.gamerack.rack.copy()
                self.gamerack.insert_piece(
                    rack_copy, move[0], move[1], self.gamerack.players_color)
                new_value = self.minimax(
                    rack_copy, depth - 1, -math.inf, math.inf, True)
                value = min(value, new_value)
                beta = min(beta, new_value)
                if beta <= alpha:
                    break
            return value

    def choose_best_move(self, rack, piece):
        """This function chooses the move that has the best score.
        Returns: best move as list [row, column]."""
        best_score = -1000
        best_move = []
        for place in self.gamerack.next_move(rack):
            rack_copy = rack.copy()
            self.gamerack.insert_piece(rack_copy, place[0], place[1], piece)
            #score = self.score_for_moves(rack_copy, piece)
            score = self.minimax(rack.copy, 10, -math.inf, math.inf, True)
            if score > best_score:
                best_score = score
                best_move = place
        return best_move