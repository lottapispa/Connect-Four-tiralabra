import unittest
from mainloop import GameLoop
from gamestatus import GameStatus
from minimax import Minimax


class TestGameLoop(unittest.TestCase):
    """Tests class gameloop."""

    def setUp(self):
        pass

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

    def main_yes(self):
        """Tests if variable self.turn is true, when self.who_starts is yes."""
        self.game = GameLoop()
        self.game.who_starts = "yes"
        self.assertTrue(self.game.turn)

    def main_no(self):
        """Tests if variable self.turn is false, when self.who_starts is no."""
        self.game = GameLoop()
        self.game.who_starts = "no"
        self.assertFalse(self.game.turn)

    def main_who_value_error(self):
        """Tests if function raises value error for wrong input word."""
        self.game = GameLoop()
        self.game.who_starts = "n"
        self.assertRaises(ValueError, self.game.main())

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
