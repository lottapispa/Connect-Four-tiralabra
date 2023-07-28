
class GameStatus:
    """Class that creates the gamerack and keeps track of the score."""

    def __init__(self):
        """Class constructor, creates variables."""
        self.rows = 6
        self.columns = 7
        # The rack is an empty matrix. Each list within the main list is a row.
        self.rack = [[0, 0, 0, 0, 0, 0, 0] for i in range(self.rows)]
        self.over = False
        self.previous_move = None

    def insert_piece(self, row: int, column: int, color: str):
        """Inserts a piece to the rack."""
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
        zeros = any(0 in i for i in self.rack)
        # print for testing
        if zeros is True:
            self.over = False
        else:
            self.over = True
        return self.over

# for testing
if __name__ == "__main__":
    x = GameStatus()
    print(x.rack)
    x.rack = [["yellow", "red", "yellow", "red", "yellow", "red", "yellow"], ["red", "yellow", "red", "yellow", "red", "yellow", "red"], ["red", "yellow", "red", "yellow", "red", "yellow", "red"], [
        "yellow", "red", "yellow", "red", "yellow", "red", "yellow"], ["yellow", "red", "yellow", "red", "yellow", "red", "yellow"], ["red", "yellow", "red", "yellow", "red", "yellow", "red"]]
    print(x.rack)
    x.is_game_over()
