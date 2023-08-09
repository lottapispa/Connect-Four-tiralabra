from gamestatus import GameStatus
from gamerack import GameRack
from minimax import Minimax


class GameLoop:
    """Class that creates the main loop of the game."""

    def __init__(self):
        """Class constructor, creates variables."""
        self.gamestatus = GameStatus()
        self.gamerack = GameRack()
        self.minimax = Minimax()
        self.who_starts = None
        self.players_color = None #self.gamerack.players_color
        self.ai_color = None #self.gamerack.ai_color
        self.turn = None #self.gamerack.turn  # true for player's turn, false for ai's turn

    def main(self):
        """Loop takes inputs from the user, starts the game and switches turns."""
        while True:
            self.players_color = input("Choose your pawn's color: 'red' or 'yellow'. ")
            if self.players_color == "red":
                self.ai_color = "yellow"
                break
            elif self.players_color == "yellow":
                self.ai_color = "red"
                break
            else:
                print("Wrong input, color needs to be red or yellow!")
                continue

        while True:
            self.who_starts = input(
            "Do you want the first move? Type 'yes' or 'no'. ")
            if self.who_starts == "yes":
                self.turn = True
                break
            elif self.who_starts == "no":
                self.turn = False
                break
            else:
                print("Wrong input, answer needs to be yes or no!")
                continue

        while self.gamestatus.is_game_over() is False:
            if self.turn is True:
                print("Player make your move: ")
                self.gamerack.print_rack()
                while True:
                    row = int(input("First choose row (1-6): "))
                    if 1 <= row <= 6:
                        column = int(input("and then choose column (1-7): "))
                        if 1 <= column <= 7:
                            break
                        else:
                            print("Wrong input, columns are 1-7!")
                            continue
                    else:
                        print("Wrong input, rows are 1-6!")
                        continue
                self.gamestatus.insert_piece(row, column, self.players_color)
                status = self.gamestatus.is_game_over()
                if self.gamestatus.tie is True:
                    print("It's a tie!")
                    break
                elif status is True:
                    print("You win!")
                    break
                self.turn = False
            if self.turn is False:
                # call minimax
                row, column = None
                self.gamestatus.insert_piece(row, column, self.ai_color)
                status = self.gamestatus.is_game_over()
                if self.gamestatus.tie is True:
                    print("It's a tie!")
                    break
                elif status is True:
                    print("You lose!")
                    break
                self.turn = True
            else:
                raise ValueError("Variable self.turn doesn't work right!")

# for testing
if __name__ == "__main__":
    game = GameLoop()
    game.main()
