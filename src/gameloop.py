from gamestatus import GameStatus
from gamerack import GameRack
from minimax import Minimax
from score import Score
import math
import time

class GameLoop:
    """Class that creates the main loop of the game."""

    def __init__(self):
        """Class constructor, creates variables."""
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.minimax = Minimax(self.gamerack, self.gamestatus)
        self.score = Score(self.gamerack, self.gamerack.players_color)
        self.who_starts = None
        self.turn = None # true for player's turn, false for ai's turn
        self.depth = 10 #?
        self.running = None

    def start_inputs(self):
        """This function takes start inputs from user."""
        self.running = True
        while self.running:
            self.gamerack.players_color = input("Choose your pawn's color: 'R' for red or 'Y' for yellow. ")
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
                print("Player make your move: ")
                self.gamerack.print_rack()
                while True:
                    try:
                        row = input("First choose row (1-6): ")
                        row = int(row)
                        if 1 <= row <= 6:
                            if self.gamerack.is_valid(row-1, None):
                                break
                            elif self.gamerack.is_valid(row-1, None) is False:
                                print("Wrong input, you can't put your piece there!")
                                continue
                        else:
                            print("Wrong input, rows are 1-6!")
                    except ValueError:
                        print("Wrong input, rows are 1-6!")
                while True:
                    try:
                        column = input("and then choose column (1-7): ")
                        column = int(column)
                        if 1 <= column <= 7:
                            if self.gamerack.is_valid(row-1, column-1):
                                break
                            elif self.gamerack.is_valid(row-1, column-1) is False:
                                print("Wrong input, the spot is taken you can't put your piece there!")
                                continue
                        else:
                            print("Wrong input, columns are 1-7!")
                    except ValueError:
                        print("Wrong input, columns are 1-7!")
  
                self.gamerack.insert_piece(self.gamerack.rack, row-1, column-1, self.gamerack.players_color)
                self.gamestatus.is_game_over(self.gamerack.rack)
                if self.gamestatus.status == 0:
                    print("It's a tie!")
                    break
                elif self.gamestatus.status == -100:
                    print("You win!")
                    break
                self.turn = False
            if self.turn is False:
                # call minimax
                result = self.minimax.minimax(self.gamerack.rack, self.depth, -math.inf, math.inf, True)
                row, column = result[0], result[1]
                self.gamerack.insert_piece(self.gamerack.rack, row, column, self.gamerack.ai_color)
                status = self.gamestatus.is_game_over(self.gamerack.rack)
                if self.gamestatus.status == 0:
                    print("It's a tie!")
                    break
                elif self.gamestatus.status == 100:
                    print("You lose!")
                    break
                self.turn = True
            else:
                raise ValueError("Variable self.turn doesn't work right!")

# for testing
if __name__ == "__main__":
    game = GameLoop()
    #rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [0, "Y", "R", "R", 0, 0, 0], [0, "Y", "R", "R", "Y", 0, 0]]
    #rack1 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, "R", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [0, "Y", "R", "R", 0, 0, 0], [0, "Y", "R", "R", "Y", 0, 0]]
    #rack2 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [0, "Y", "R", "R", 0, 0, 0], [0, "Y", "R", "R", "Y", "R", 0]]
    #game.gamerack.ai_color = "R"
    #game.gamerack.players_color = "Y"
    #print(game.score.score_for_moves(rack, game.gamerack.ai_color))
    #print(game.score.score_for_moves(rack1, game.gamerack.ai_color))
    #print(game.score.score_for_moves(rack2, game.gamerack.ai_color))
    #print(game.score.choose_best_move(rack, game.gamerack.ai_color))
    #game.main()
