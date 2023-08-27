class GameRack:
    """Class that creates and keeps track of the gamerack."""

    def __init__(self, rack):
        """Class constructor, creates variables."""
        self.rows = 6
        self.columns = 7
        self.rack = rack
        self.players_color = None
        self.ai_color = None

    def insert_piece(self, rack, row: int, column: int, color: str):
        """Inserts a piece to the rack."""
        if color not in ("R", "Y"):
            raise ValueError("Wrong input, color needs to be red or yellow!")
        if not 0 <= row <= 5:
            raise ValueError("Wrong input, rows are 1-6!")
        if not 0 <= column <= 6:
            raise ValueError("Wrong input, columns are 1-7!")
        #if [row, column] in self.next_move(rack):
        rack[row][column] = color
        #else:
        #    raise ValueError("Wrong input, you can't put your piece there!")

    def next_move(self, rack: list):
        """This function finds all possible locations a player can put their piece in during their turn.
        It works by counting the last 0 (empty slot) of each column, except for bottom row."""
        self.possible_moves = []
        row_count = 0
        for column in range(0, self.columns):
            last_zero = None
            for row in rack:
                if row[column] == 0:
                    last_zero = [row_count, column]
                row_count += 1
            row_count = 0
            if last_zero is not None:
                self.possible_moves.append(last_zero)
        return self.possible_moves

    def is_valid(self, column):
        """This function tests if column is valid.
        Returns: row of that column if it's valid, otherwise false."""
        for place in self.next_move(self.rack):
            if place[1] == column:
                return place[0]
        return False

    def print_rack(self):
        """This function prints the gamerack."""
        for row in self.rack:
            print(row)
