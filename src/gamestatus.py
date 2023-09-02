class GameStatus:
    """Class that keeps track of the status of the game."""

    def __init__(self, gamerack):
        """Class constructor, creates variables."""
        self.gamerack = gamerack
        self.rows = self.gamerack.rows
        self.columns = self.gamerack.columns
        self.winner = None
        self.status = None

    def check_for_win_hor(self, rack: list, piece):
        """Checks for a connect four horizontally.
        Returns: True for there is a win, False for no win."""
        self.winner = None
        counter = 0
        for row in rack:
            for column in row:
                if column == piece:
                    counter += 1
                else:
                    counter = 0
                    continue
                if counter >= 4:
                    self.winner = piece
                    return True
        return False

    def check_for_win_ver(self, rack: list, piece):
        """Checks for a connect four vertically.
        Returns: True for there is a win, False for no win."""
        self.winner = None
        counter = 0
        for column in range(self.columns):
            for row in rack:
                if row[column] == piece:
                    counter += 1
                else:
                    counter = 0
                    continue
                if counter >= 4:
                    self.winner = piece
                    return True
        return False

    def check_for_win_dia(self, rack: list, piece):
        """Checks for a connect four diagonally.
        Returns: True for there is a win, False for no win."""
        self.winner = None
        for column in range(self.columns-3):
            for row in range(self.rows-3):
                if rack[row][column] == piece and rack[row+1][column+1] == piece and rack[row+2][column+2] == piece and rack[row+3][column+3] == piece:
                    self.winner = piece
                    return True
        for column in range(self.columns-3):
            for row in range(3, self.rows):
                if rack[row][column] == piece and rack[row-1][column+1] == piece and rack[row-2][column+2] == piece and rack[row-3][column+3] == piece:
                    self.winner = piece
                    return True
        return False

    def check_for_tie(self, rack: list):
        """Checks for a tie. Returns: True if it's a tie, False if not."""
        for row in rack:
            for column in row:
                if column == 0:
                    return False
        if self.winner is None:
            return True

    def is_game_over(self, rack: list):
        """Combines win check and tie check functions.
        Returns: True if game is over, False if not."""
        self.status = None
        if self.check_for_win_hor(rack, self.gamerack.players_color) or self.check_for_win_ver(rack, self.gamerack.players_color) or self.check_for_win_dia(rack, self.gamerack.players_color):
            self.status = -1000
            return True
        if self.check_for_win_hor(rack, self.gamerack.ai_color) or self.check_for_win_ver(rack, self.gamerack.ai_color) or self.check_for_win_dia(rack, self.gamerack.ai_color):
            self.status = 1000
            return True
        if self.check_for_tie(rack) is True:
            self.status = 0
            return True
        else:
            return False
