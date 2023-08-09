import unittest
from unittest import mock
from gameloop import GameLoop
from gamestatus import GameStatus
from minimax import Minimax


class TestGameLoop(unittest.TestCase):
    """Tests class gameloop."""

    def setUp(self):
        self.game = GameLoop()

    def test_init(self):
        self.game = GameLoop()
        self.game.gamestatus = GameStatus()
        self.game.minimax = Minimax()
        self.game.who_starts = None
        self.game.players_color = None
        self.game.ai_color = None
        self.game.turn = None
        self.assertEqual(self.game.who_starts, None)
        self.assertEqual(self.game.players_color, None)
        self.assertEqual(self.game.ai_color, None)
        self.assertEqual(self.game.turn, None)

    @mock.patch("mainloop.input", create=True)
    def main(self, mocked_input):
        """Tests if variable self.turn is true, when self.who_starts is yes."""
        mocked_input.side_effect = ["yes"]
        self.game.main()
        self.assertTrue(self.game.turn)
        mocked_input.side_effect = ["no"]
        self.game.main()
        self.assertFalse(self.game.turn)
        mocked_input.side_effect = ["yes", "no"]
        self.game.main()
        self.assertRaises(ValueError)

    def main_who_value_error(self):
        """Tests if function raises value error for wrong input word."""
        pass

    def main_red(self):
        """Tests if variable self.ai_color is yellow, when self.players_color is red."""
        self.game = GameLoop()
        self.game.players_color = "red"
        self.assertEqual(self.game.ai_color, "yellow")

    def main_red(self):
        """Tests if variable self.ai_color is red, when self.players_color is yellow."""
        self.game = GameLoop()
        self.game.players_color = "yellow"
        self.assertEqual(self.game.ai_color, "red")

    def main_color_value_error(self):
        """Tests if function raises value error for wrong input color."""
        self.game = GameLoop()
        self.game.players_color = "5"
        self.assertRaises(ValueError, self.game.players_color)

    def while_loop(self):
        """Tests while loop."""
        self.game = GameLoop()
        self.game.gamestatus.is_game_over = False
        self.game.turn = True

