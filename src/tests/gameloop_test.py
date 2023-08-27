import unittest
from unittest.mock import patch
import io
from unittest.mock import *
from gameloop import GameLoop
from gamerack import GameRack
from gamestatus import GameStatus
from minimax import Minimax
from score import Score


class TestGameLoop(unittest.TestCase):
    """Tests class gameloop."""

    def setUp(self):
        self.game = GameLoop()

    def test_init(self):
        self.game = GameLoop()
        self.game.gamestatus = GameStatus(self.game.gamerack)
        self.game.score = Score(self.game.gamerack, self.game.gamestatus)
        self.game.minimax = Minimax(self.game.gamerack, self.game.gamestatus, self.game.score)
        self.game.who_starts = None
        self.game.gamerack.players_color = None
        self.game.gamerack.ai_color = None
        self.game.turn = None
        self.assertEqual(self.game.who_starts, None)
        self.assertEqual(self.game.gamerack.players_color, None)
        self.assertEqual(self.game.gamerack.ai_color, None)
        self.assertEqual(self.game.turn, None)

    @patch("builtins.input", side_effect=["R", "yes"])
    def test_start_inputs_red(self, mock_input):
        """Tests if variable self.ai_color is yellow, when self.players_color is red and if variable who_starts is correct."""
        self.game = GameLoop()
        self.game.start_inputs()
        self.assertEqual(self.game.gamerack.players_color, "R")
        self.assertEqual(self.game.gamerack.ai_color, "Y")
        self.assertEqual(self.game.who_starts, "yes")
        self.assertTrue(self.game.turn)
        self.assertFalse(self.game.running)

    @patch("builtins.input", side_effect=["Y", "no"])
    def test_start_inputs_yellow(self, mock_input):
        """Tests if variable self.ai_color is red, when self.players_color is yellow and if variable who_starts is correct."""
        self.game = GameLoop()
        self.game.start_inputs()
        self.assertEqual(self.game.gamerack.players_color, "Y")
        self.assertEqual(self.game.gamerack.ai_color, "R")
        self.assertEqual(self.game.who_starts, "no")
        self.assertFalse(self.game.turn)
        self.assertFalse(self.game.running)

    @patch("builtins.input", side_effect=["X", "Y", "yes"])
    def start_inputs_wrong(self, mock_input):
        """Tests if ValueError is raised when input is wrong."""
        self.game = GameLoop()
        expected_output = ["Wrong input, color needs to be red or yellow!",
                           "Choose your pawn's color: 'R' for red or 'Y' for yellow. ", "Do you want the first move? Type 'yes' or 'no'. "]
        self.game.start_inputs()
        self.assertEqual(mock_input.call_count, 3)
        self.assertEqual(self.game.gamerack.players_color, "Y")
        self.assertEqual(self.game.gamerack.ai_color, "R")
        self.assertEqual(self.game.who_starts, "yes")
        self.assertTrue(self.game.turn)
        self.assertFalse(self.game.running)
        self.assertEqual([call[0] for call in mock_input.call_args_list], [
                         "X", "Y", "yes"])
        self.assertEqual([call[0] for call in self.game.start_inputs(
        ).print.call_args_list], expected_output)

    @patch("builtins.input", side_effect=["5", "5"])
    def test_players_move_correct_number(self, mock_input):
        self.game = GameLoop()
        self.game.players_move()
        self.assertEqual(self.game.players_move(), (5, 4))

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["9", "5", "5"])
    def players_move_wrong_number(self, mock_stdout, mock_input):
        self.game = GameLoop()
        self.game.players_move()
        assert mock_stdout.getvalue() == "Wrong input, columns are 1-7!\n"
        self.assertEqual(self.game.players_move(), (5, 4))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_prints_lose(self, mock_stdout):
        self.game = GameLoop()
        self.game.gamestatus.status = 1000
        self.game.end_prints()
        assert mock_stdout.getvalue() == "You lose!\n"

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_prints_win(self, mock_stdout):
        self.game = GameLoop()
        self.game.gamestatus.status = -1000
        self.game.end_prints()
        assert mock_stdout.getvalue() == "You win!\n"

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end_prints_tie(self, mock_stdout):
        self.game = GameLoop()
        self.game.gamestatus.status = 0
        self.game.end_prints()
        assert mock_stdout.getvalue() == "It's a tie!\n"

    @patch("builtins.input", side_effect=["6", "4"])
    def main_loop(self, mock_input):
        """Tests main loop."""
        self.game = GameLoop()
        self.game.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, "Y", 0, 0, 0, 0], [0, 0, "R", 0, 0, 0, 0], [0, 0, "R", "Y", 0, 0, 0]]
        self.game.turn = True
        self.game.main()
        # TestGameLoop.test_start_inputs_red()
