import math
from gamestatus import GameStatus
from gamerack import GameRack
from minimax import Minimax
from score import Score

class GameLoop:
    """Class that creates the main loop of the game."""

    def __init__(self):
        """Class constructor, creates variables."""
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.score = Score(self.gamerack, self.gamestatus)
        self.minimax = Minimax(self.gamerack, self.gamestatus, self.score)
        self.who_starts = None
        self.turn = None  # true for player's turn, false for ai's turn
        self.running = None

    def start_inputs(self):
        """This function takes start inputs from user."""
        self.running = True
        while self.running:
            self.gamerack.players_color = input(
                "Choose your pawn's color: 'R' for red or 'Y' for yellow. ")
            if self.gamerack.players_color == "R":
                self.gamerack.ai_color = "Y"
                self.running = False
            elif self.gamerack.players_color == "Y":
                self.gamerack.ai_color = "R"
                self.running = False
            else:
                print("Wrong input, color needs to be red or yellow!")
                continue

        self.running = True
        while self.running:
            self.who_starts = input(
                "Do you want the first move? Type 'yes' or 'no'. ")
            if self.who_starts == "yes":
                self.turn = True
                self.running = False
            elif self.who_starts == "no":
                self.turn = False
                self.running = False
            else:
                print("Wrong input, answer needs to be yes or no!")
                continue

    def main(self):
        """Loop starts the game and switches turns."""
        self.start_inputs()
        while self.gamestatus.is_game_over(self.gamerack.rack) is False:

            if self.turn is True:
                self.gamerack.print_rack()
                row, column = self.players_move()
                self.gamerack.insert_piece(
                    self.gamerack.rack, row, column, self.gamerack.players_color)
                if self.gamestatus.is_game_over(self.gamerack.rack):
                    self.end_prints()
                    break
                self.turn = False

            # ai's move
            if self.turn is False:
                # works at least until here
                move = self.minimax.choose_best_move(
                    self.gamerack.rack, self.gamerack.ai_color)
                self.gamerack.insert_piece(
                    self.gamerack.rack, move[0], move[1], self.gamerack.ai_color)
                if self.gamestatus.is_game_over(self.gamerack.rack):
                    self.end_prints()
                    break
                self.turn = True
            else:
                raise ValueError("Variable self.turn doesn't work right!")

    def players_move(self):
        """Asks for player's move. Returns: row and column."""
        while True:
            try:
                column = input(
                    "Player make your move, choose column (1-7): ")
                column = int(column)
                if 1 <= column <= 7:
                    if self.gamerack.is_valid(column-1) is False:
                        print("Wrong input, column is full!")
                        continue
                    else:
                        row = self.gamerack.is_valid(column-1)
                        return row, column-1
                else:
                    print("Wrong input, columns are 1-7!")
            except ValueError:
                print("Wrong input, columns are 1-7!")

    def end_prints(self):
        """Prints status of the game to user when game ends."""
        if self.gamestatus.status == 1000:
            print("You lose!")
        elif self.gamestatus.status == -1000:
            print("You win!")
        else:
            print("It's a tie!")


# for testing
if __name__ == "__main__":
    game = GameLoop()
    game.main()
