class GameRack:
    """Class that creates and keeps track of the gamerack."""

    def __init__(self):
        """Class constructor, creates variables."""
        self.rows = 6
        self.columns = 7
        # The rack is an empty matrix. Each list within the main list is a row. Last row is the bottom row.
        self.rack = [[0, 0, 0, 0, 0, 0, 0] for i in range(self.rows)]
        self.players_color = None
        self.ai_color = None

    def insert_piece(self, rack, row: int, column: int, color: str):
        """Inserts a piece to the rack."""
        if color not in ("R", "Y"):
            raise ValueError("Wrong input, color needs to be red or yellow!")
        if not 1 <= row <= 6:
            raise ValueError("Wrong input, rows are 1-6!")
        if not 1 <= column <= 7:
            raise ValueError("Wrong input, columns are 1-7!")
        # if row is 1 the index is 0, and column 1's index is 0
        if [row-1, column-1] in self.next_move(rack):
            rack[row-1][column-1] = color
        else:
            raise ValueError("Wrong input, you can't put your piece there!")

    def next_move(self, rack):
            """This function finds all possible locations a player can put their piece in during their turn.
            It works by counting the last 0 (empty slot) of each column, except for bottom row."""
            # this list will contain indexes of possible locations like this [[0,0], [0,1]]. Since indexes start from 0, rows are 0-5 and columns are 0-6.
            self.possible_moves = [] # this list needs to be here so it resets every time it's called
            last_zero = None
            row_count = 0
            for column in range(0, self.columns):
                for row in rack:
                    if row[column] == 0:
                        last_zero = [row_count, column]
                    row_count += 1
                row_count = 0
                self.possible_moves.append(last_zero)
            return self.possible_moves
    
    def is_valid(self, place, axis):
        place -= 1
        if axis == "row":
            for i in self.next_move(self.rack):
                if place == i[0]:
                    return True
            return False
        else:
            for i in self.next_move(self.rack):
                if place == i[1]:
                    return True
            return False

    def print_rack(self):
        """This function prints the gamerack."""
        for row in self.rack:
            print(row)
