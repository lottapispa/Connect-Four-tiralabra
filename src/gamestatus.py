from gamerack import GameRack

class GameStatus:
    """Class that keeps track of the status of the game."""

    def __init__(self, gamerack):
        """Class constructor, creates variables."""
        self.gamerack = gamerack
        self.rack = self.gamerack.rack
        self.rows = self.gamerack.rows
        self.columns = self.gamerack.columns
        self.over = False
        self.winner = None
        self.status = None # 0 for tie, 1 for ai win and player loss, -1 for player win and ai loss

    def check_for_win_hor(self):
        """Checks for a connect four horizontally.
        Returns: True for there is a win, False for no win."""
        counter = 1
        previous = None
        for row in self.rack:
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

    def check_for_win_ver(self):
        """Checks for a connect four vertically.
        Returns: True for there is a win, False for no win."""
        counter = 1
        previous = None
        for column in range(1, self.columns):
            for row in self.rack:
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

    def check_for_win_dia(self):
        """Checks for a connect four diagonally.
        Returns: True for there is a win, False for no win."""
        for column in range(self.columns-3):
            for row in range(self.rows-3):
                if self.rack[row][column] == "R" and self.rack[row+1][column+1] == "R" and self.rack[row+2][column+2] == "R" and self.rack[row+3][column+3] == "R":
                    self.winner = "R"
                    return True
                if self.rack[row][column] == "Y" and self.rack[row+1][column+1] == "Y" and self.rack[row+2][column+2] == "Y" and self.rack[row+3][column+3] == "Y":
                    self.winner = "Y"
                    return True
        for column in range(self.columns-3):
            for row in range(3, self.rows):
                if self.rack[row][column] == "R" and self.rack[row-1][column+1] == "R" and self.rack[row-2][column+2] == "R" and self.rack[row-3][column+3] == "R":
                    self.winner = "R"
                    return True
                if self.rack[row][column] == "Y" and self.rack[row-1][column+1] == "Y" and self.rack[row-2][column+2] == "Y" and self.rack[row-3][column+3] == "Y":
                    self.winner = "Y"
                    return True
        return False
    
    def is_game_over(self):
        """If rack is full or a player connects four, variable over is True.
        Returns: boolean self.over."""
        zeros = 0  # any(0 in i for i in self.rack)
        for row in self.rack:
            z = row.count(0)
            zeros += z
        horizontal = self.check_for_win_hor()
        vertical = self.check_for_win_ver()
        diagonal = self.check_for_win_dia()
        if True in [horizontal, vertical, diagonal]:
            if self.winner == self.gamerack.players_color:
                self.status = -1
            elif self.winner == self.gamerack.ai_color:
                self.status = 1
            self.over = True
            return self.over
        # if there's no zeros or connect fours on the rack, the rack is full and it's a tie
        elif self.over is False and zeros == 0:
            self.over = True
            self.status = 0
            return self.over
        else:
            self.over = False
            return self.over
