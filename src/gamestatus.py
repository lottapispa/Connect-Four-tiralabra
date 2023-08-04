
class GameStatus:
    """Class that creates the gamerack and keeps track of the status of the game."""

    def __init__(self):
        """Class constructor, creates variables."""
        self.rows = 6
        self.columns = 7
        # The rack is an empty matrix. Each list within the main list is a row. First row is the bottom row.
        self.rack = [[0, 0, 0, 0, 0, 0, 0] for i in range(self.rows)]
        self.over = False
        self.tie = False
        self.possible_moves = []

    def insert_piece(self, row: int, column: int, color: str):
        """Inserts a piece to the rack."""
        # This function does not check if spot is actually possible
        if color not in ("red", "yellow"):
            raise ValueError("Wrong input, color needs to be red or yellow!")
        if not 1 <= row <= 6:
            raise ValueError("Wrong input, rows are 1-7!")
        if not 1 <= column <= 7:
            raise ValueError("Wrong input, columns are 1-6!")
        # if row is 1 the index is 0, and column 1's index is 0
        # if there is already a piece in the index, you can't change it
        if self.rack[row-1][column-1] != 0:
            raise ValueError("Wrong input, that spot already has a piece!")
        self.rack[row-1][column-1] = color
        self.previous_move = [row, column, color]

    def is_game_over(self):
        """If rack is full or a player connects four, variable over is True.
        Returns: boolean self.over."""
        zeros = 0 # any(0 in i for i in self.rack)
        for row in self.rack:
            z = row.count(0)
            zeros += z
        horizontal = self.check_for_win_hor()
        vertical = self.check_for_win_ver()
        diagonal = self.check_for_win_dia()
        if True in [horizontal, vertical, diagonal]:
            self.over = True
            return self.over
        # if there's no zeros or connect fours on the rack, the rack is full and it's a tie
        #elif self.over is False and zeros == 0:
        #    self.over = True
        #    self.tie = True
        #    return self.over
        else:
            self.over = False
            return self.over
    
    def check_for_win_hor(self):
        """Checks for a connect four horizontally. Returns: True for there is a win, False for no win."""
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
                    return True
                previous = i
        return False
        
    def check_for_win_ver(self):
        """Checks for a connect four vertically. Returns: True for there is a win, False for no win."""
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
                    return True
                previous = row[column]
        return False
    
    def check_for_win_dia(self):
        """Checks for a connect four diagonally. Returns: True for there is a win, False for no win."""
        for column in range(self.columns-3):
            for row in range(self.rows-3):
                if self.rack[row][column] == "red" and self.rack[row+1][column+1] == "red" and self.rack[row+2][column+2] == "red" and self.rack[row+3][column+3] == "red":
                    return True
                elif self.rack[row][column] == "yellow" and self.rack[row+1][column+1] == "yellow" and self.rack[row+2][column+2] == "yellow" and self.rack[row+3][column+3] == "yellow":
                    return True
        for column in range(self.columns-3):
            for row in range(3, self.rows):
                if self.rack[row][column] == "red" and self.rack[row-1][column+1] == "red" and self.rack[row-2][column+2] == "red" and self.rack[row-3][column+3] == "red":
                    return True
                elif self.rack[row][column] == "yellow" and self.rack[row-1][column+1] == "yellow" and self.rack[row-2][column+2] == "yellow" and self.rack[row-3][column+3] == "yellow":
                    return True
        return False
    
    def next_move(self):
        """This function finds all possible locations a player can put their piece in during their turn."""
        self.possible_moves = []
        for row in self.rack:
            for place in row:
                if place != 0:
                    #spot is already taken
                    pass

# for testing
if __name__ == "__main__":
    game = GameStatus()
    #game.rack, [[0, 0, "red", "yellow", "yellow", 0, 0], [0, 0, "red", "red", 0, 0, 0], [0, 0, "yellow", 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
