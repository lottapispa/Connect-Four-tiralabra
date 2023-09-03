class GameRack:
    """Class that creates and keeps track of the gamerack."""

    def __init__(self, rack):
        """Class constructor, creates variables."""
        self.rows = 6
        self.columns = 7
        self.rack = rack
        self.players_color = None
        self.ai_color = None
        self.possible_moves = []

    def insert_piece(self, rack, row: int, column: int, color: str):
        """Inserts a piece to the rack."""
        if color not in ("R", "Y"):
            raise ValueError("Wrong input, color needs to be red or yellow!")
        if not 0 <= row <= 5:
            raise ValueError("Wrong input, rows are 1-6!")
        if not 0 <= column <= 6:
            raise ValueError("Wrong input, columns are 1-7!")
        rack[row][column] = color

    def next_move(self, rack: list):
        """This function finds all possible locations the ai can put its piece in during its turn.
        It works by counting the last 0 (empty slot) of each column. Returns: a list."""
        self.possible_moves = []
        row_count = 0
        switch = True
        column = 3
        minus = 1
        add = 2
        while 0 <= column <= 6:
            last_zero = None
            for row in rack:
                if row[column] == 0:
                    last_zero = [row_count, column]
                row_count += 1
            row_count = 0
            if last_zero is not None:
                self.possible_moves.append(last_zero)
            if switch is True:
                column -= minus
                minus += 2
                switch = False
            else:
                column += add
                add += 2
                switch = True
        return self.possible_moves

    def is_valid(self, rack, column):
        """This function tests if column is valid.
        Returns: row of that column if it's valid, otherwise False."""
        for place in self.next_move(rack):
            if place[1] == column:
                return place[0]
        return False

    def print_rack(self, rack):
        """This function prints the gamerack."""
        for row in rack:
            print('[%s]' % ', '.join(map(str, row)))
