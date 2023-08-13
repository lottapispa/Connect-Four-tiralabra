class Score:
    """Class that is going to analyse the state of the gamerack and give scores to possible moves."""

    def __init__(self, gamerack, color):
        """Class constructor, creates variables."""
        self.gamerack = gamerack
        self.color = color
        self.score = None
        moves_count = 21 # per player

    def winning_move(self):
        """This function checks if the next move will connect four and win."""
        pass

    def heuristic_value(self):
        """This function makes rules for how to get different scores, by giving better value the quicker the win."""
        rack_copy = self.gamerack.rack.copy()
        for i in self.gamerack.next_move(self.gamerack.rack):
            self.gamerack.insert_piece(rack_copy, i[0], i[1], self.color)
            #self.score = 

    def score_for_location(self):
        """This function gives scores to all the possible moves."""
        scores = []
        # call heuristic_value()
        return scores

    def choose_move(self):
        """This function chooses the move that has the best score."""
        return max(self.score_for_location())
