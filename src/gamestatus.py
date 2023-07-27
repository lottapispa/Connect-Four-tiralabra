
class GameStatus:
    """Class that creates the gamerack and keeps track of the score."""
    def __init__(self):
        """Class constructor, creates variables."""
        self.rows = 6
        self.columns = 7
        # The rack is an empty matrix. Each list within the main list is a row.
        self.rack = [[0, 0, 0, 0, 0, 0, 0] for i in range(self.rows)]

    def insert_piece(self, row: int, column: int, color: str):
        """Inserts a piece to the rack."""
        if color != "blue" and color != "red":
            raise ValueError("Wrong input, color needs to be blue or red!")
        if not 1 <= row <= 6:
            raise ValueError("Wrong input, rows are 1-7!")
        if not 1 <= column <= 7:
            raise ValueError("Wrong input, columns are 1-6!")
        # if row is 1 the index is 0, and column 1's index is 0
        # if there is already a piece in the index, you can't change it
        if self.rack[row-1][column-1] != 0:
            raise ValueError("Wrong input, that spot already has a piece!")
        else:
            #self.rack[row-1][column-1] = color
            self.rack[row-1].insert(column-1, color)

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
    x = GameStatus()
    print(x.rack)
    x.insert_piece(1, 2, "blue")
    print(x.rack)