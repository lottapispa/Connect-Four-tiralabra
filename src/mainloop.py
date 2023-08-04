from gamestatus import GameStatus
from minimax import Minimax

class GameLoop:
    """Class that creates the main loop of the game."""

    def __init__(self):
        """Class constructor, creates variables."""
        self.gamestatus = GameStatus()
        self.minimax = Minimax()
        self.turn = None # true for player's turn, false for ai's turn

    def main(self):
        """Loop takes inputs from the user, starts the game and switches turns."""
        who_starts = input("Do you want the first move? Type 'yes' or 'no'. ")
        if who_starts == "yes":
            self.turn = True
        elif who_starts == "no":
            self.turn = False
        else:
            raise ValueError("Wrong input, answer needs to be yes or no!")
        players_color = input("Choose color: 'red' or 'yellow'. ")
        if players_color == "red":
            ai_color = "yellow"
        elif players_color == "yellow":
            ai_color = "red"
        else:
            raise ValueError("Wrong input, color needs to be red or yellow!")
        while self.gamestatus.is_game_over() is False:
            if self.turn is True:
                print("Player make your move: ")
                row = int(input("First choose row (1-6): "))
                column = int(input("and then choose column (1-7): "))
                self.gamestatus.insert_piece(row, column, players_color)
                status = self.gamestatus.is_game_over()
                if self.gamestatus.tie == True:
                    print("It's a tie!")
                    break
                elif status == True:
                    print("You win!")
                    break
                self.turn = False
            if self.turn == False:
                # call minimax
                row, column = None
                self.gamestatus.insert_piece(row, column, ai_color)
                status = self.gamestatus.is_game_over()
                if self.gamestatus.tie == True:
                    print("It's a tie!")
                    break
                elif status == True:
                    print("You lose!")
                    break
                self.turn = True
            else:
                raise ValueError("Variable self.turn doesn't work right!")

# for testing
if __name__ == "__main__":
    game = GameLoop()
    game.main()