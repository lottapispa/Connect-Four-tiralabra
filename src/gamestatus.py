class GameStatus:
    """Class that keeps track of the status of the game."""

    def __init__(self, gamerack):
        """Class constructor, creates variables."""
        self.gamerack = gamerack
        self.rows = self.gamerack.rows
        self.columns = self.gamerack.columns
        self.winner = None
        self.status = None # 0 for tie, 1 for ai win and player loss, -1 for player win and ai loss

    def check_for_win_hor(self, rack):
        """Checks for a connect four horizontally.
        Returns: True for there is a win, False for no win."""
        counter = 1
        previous = None
        for row in rack:
            for i in row:
                if i == 0:
                    previous = i
                    continue
                if previous == i:
                    counter += 1
                else:
                    counter = 1
                if counter >= 4:
                    self.winner = previous
                    return True
                previous = i
        return False

    def check_for_win_ver(self, rack):
        """Checks for a connect four vertically.
        Returns: True for there is a win, False for no win."""
        counter = 1
        previous = None
        for column in range(1, self.columns):
            for row in rack:
                if row[column] == 0:
                    previous = row[column]
                    continue
                if previous == row[column]:
                    counter += 1
                else:
                    counter = 1
                if counter >= 4:
                    self.winner = previous
                    return True
                previous = row[column]
        return False

    def check_for_win_dia(self, rack):
        """Checks for a connect four diagonally.
        Returns: True for there is a win, False for no win."""
        for column in range(self.columns-3):
            for row in range(self.rows-3):
                if rack[row][column] == "R" and rack[row+1][column+1] == "R" and rack[row+2][column+2] == "R" and rack[row+3][column+3] == "R":
                    self.winner = "R"
                    return True
                if rack[row][column] == "Y" and rack[row+1][column+1] == "Y" and rack[row+2][column+2] == "Y" and rack[row+3][column+3] == "Y":
                    self.winner = "Y"
                    return True
        for column in range(self.columns-3):
            for row in range(3, self.rows):
                if rack[row][column] == "R" and rack[row-1][column+1] == "R" and rack[row-2][column+2] == "R" and rack[row-3][column+3] == "R":
                    self.winner = "R"
                    return True
                if rack[row][column] == "Y" and rack[row-1][column+1] == "Y" and rack[row-2][column+2] == "Y" and rack[row-3][column+3] == "Y":
                    self.winner = "Y"
                    return True
        return False
    
    def is_game_over(self, rack: list):
        """If rack is full or a player connects four, variable over is True.
        Returns: boolean self.over."""
        zeros = None
        for row in rack:
            try:
                if 0 in row:
                    zeros = True
                    break
            except TypeError:
                pass
            zeros = False
        horizontal = self.check_for_win_hor(rack)
        vertical = self.check_for_win_ver(rack)
        diagonal = self.check_for_win_dia(rack)
        if True in [horizontal, vertical, diagonal]:
            if self.winner == self.gamerack.players_color:
                self.status = -1
            elif self.winner == self.gamerack.ai_color:
                self.status = 1
            return True
        # if there's no zeros or connect fours on the rack, the rack is full and it's a tie
        elif self.winner is None and zeros is False:
            self.status = 0
            return True
        else:
            return False
