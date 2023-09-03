import math
import time
from gamestatus import GameStatus
from gamerack import GameRack
from minimax import Minimax
from score import Score


class GameLoop:
    """Class that creates the main loop of the game."""

    def __init__(self):
        """Class constructor, creates variables."""
        self.rack = [[0, 0, 0, 0, 0, 0, 0] for i in range(6)]
        self.gamerack = GameRack(self.rack)
        self.gamestatus = GameStatus(self.gamerack)
        self.minimax = Minimax(self.gamerack, self.gamestatus, Score(
            self.gamerack, self.gamestatus))
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
        while True:
            if self.turn is True:
                self.gamerack.print_rack(self.rack)
                row, column = self.players_move()
                self.gamerack.insert_piece(
                    self.rack, row, column, self.gamerack.players_color)
                if self.gamestatus.is_game_over(self.rack):
                    self.gamerack.print_rack(self.rack)
                    self.end_prints()
                    break
                self.turn = False

            if self.turn is False:
                self.start = time.time()
                move, score = self.minimax.minimax(
                    self.rack, 10, -math.inf, math.inf, True, self.start)
                self.gamerack.insert_piece(
                    self.rack, move[0], move[1], self.gamerack.ai_color)
                if self.gamestatus.is_game_over(self.rack):
                    self.gamerack.print_rack(self.rack)
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
                    if self.gamerack.is_valid(self.rack, column-1) is False:
                        print("Wrong input, column is full!")
                        continue
                    row = self.gamerack.is_valid(self.rack, column-1)
                    return row, column-1
                print("Wrong input, columns are 1-7!")
            except ValueError:
                print("Wrong input, columns are 1-7!")

    def end_prints(self):
        """Prints status of the game to user when game ends."""
        if self.gamestatus.status == -1000:
            print("You win!")
        elif self.gamestatus.status == 1000:
            print("You lose!")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    game = GameLoop()
    game.main()
