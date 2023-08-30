import math


class Score:
    """Class that is going to analyse the state of the gamerack and give scores to possible moves."""

    def __init__(self, gamerack, gamestatus):
        """Class constructor, creates variables."""
        self.gamerack = gamerack
        self.gamestatus = gamestatus

    def heuristic_value(self, line, piece):
        """This function makes rules for how to get different scores, by giving better value the quicker the win.
        Only called by function score_for_moves. Returns: variable score."""
        score = 0
        opp = None
        if piece == self.gamerack.players_color:
            opp = self.gamerack.ai_color
        else:
            opp = self.gamerack.players_color

        if line.count(piece) == 4:
            score += 100
        elif line.count(piece) == 3 and line.count(0) == 1:
            score += 10
        elif line.count(piece) == 2 and line.count(0) == 2:
            score += 5

        if line.count(opp) == 3 and line.count(0) == 1:
            score -= 70
        elif line.count(opp) == 2 and line.count(0) == 2:
            score -= 7

        return score

    def score_for_moves(self, rack, piece):
        """This function gives scores to all the possible moves.
        Calls function heuristic_value. Returns: variable score."""
        score = 0

        for row in range(6):
            for column in range(7-3):
                line = [rack[row][column+i] for i in range(4)]
                score += self.heuristic_value(line, piece)

        for column in range(7):
            for row in range(6-3):
                line = [rack[row+i][column] for i in range(4)]
                score += self.heuristic_value(line, piece)

        for row in range(6-3):
            for column in range(7-3):
                line = [rack[row+i][column+i] for i in range(4)]
                score += self.heuristic_value(line, piece)
                line = [rack[row+3-i][column+i] for i in range(4)]
                score += self.heuristic_value(line, piece)
        return score
