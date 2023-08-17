class Score:
    """Class that is going to analyse the state of the gamerack and give scores to possible moves."""

    def __init__(self, gamerack, gamestatus):
        """Class constructor, creates variables."""
        self.gamerack = gamerack #class
        self.gamestatus = gamestatus #class
        moves_count = 21 # per player

    def winning_move(self, color):
        """This function checks if the next move will connect four and win.
        Returns: winning move [row, column] if there is one, otherwise false."""
        # variable here so it resets when function is called
        winning_move = None
        for i in self.gamerack.next_move(self.gamerack.rack):
            rack_copy = self.gamerack.rack.copy()
            self.gamerack.insert_piece(rack_copy, i[0], i[1], color)
            if self.gamestatus.is_game_over(rack_copy) is True and self.gamestatus.status != 0:
                winning_move = [i[0], i[1]]
                return winning_move
        return False

    def heuristic_value(self, window, piece):
        """This function makes rules for how to get different scores, by giving better value the quicker the win."""
        # window is a list of length 4
        score = 0 # for parameter piece
        opp_piece = None
        if piece == self.gamerack.players_color:
            opp_piece = self.gamerack.ai_color
        else:
            opp_piece = self.gamerack.players_color

        if window.count(piece) == 4:
            score += 20
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 10
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 5

        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score -= 8

    def score_for_move(self):
        """This function gives scores to all the possible moves."""
        scores = []
        # call heuristic_value()
        return scores

    def choose_move(self):
        """This function chooses the move that has the best score."""
        return max(self.score_for_location())
