
class GameStatus:
    """Class that creates the gamerack and keeps track of the score."""
    def __init__(self):
        """Class constructor, creates variables."""
        self.rows = 7
        self.columns = 6
        # The rack is an empty matrix. Each list within the main list is a row.
        self.rack = self.rack = [[0, 0, 0, 0, 0, 0, 0] for i in range(self.columns)]

    def insert_piece(self, row, column, color):
        """Inserts a piece to the rack."""
        if color != "blue" or color != "red":
            raise ValueError("Wrong input, color needs to be blue or red!")
        # if row is 1 the index is 0, and column 1's index is 0
        if not 1 <= row <= 7:
            raise ValueError("Wrong input, rows are 1-7!")
        if not 1 <= column <= 6:
            raise ValueError("Wrong input, columns are 1-6!")
        # if there is already a piece in the index, you can't change it
        if self.rack[row-1][column-1] != 0:
            raise ValueError("Wrong input, that spot already has a piece!")
        else:
            self.rack[row-1][column-1] = color

    def game_over(self):
        """Stops game if rack is full or a player connects four."""
        zeros = any(0 in i for i in self.rack)
        # for testing
        if zeros is True:
            print("not full")
        else:
            print("full")

# for testing
if __name__ == "__main__":
    print(GameStatus().rack)