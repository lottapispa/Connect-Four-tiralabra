import unittest
from mainloop import GameLoop

class TestGameLoop(unittest.TestCase):
    """Tests class gameloop."""

    def setUp(self):
        pass

    def test_main_yes(self):
        self.game = GameLoop()
        self.game.who_starts = "yes"
        self.assertEqual(self.game.who_starts, "yes")

    def test_main_no(self):
        self.game = GameLoop()
        self.game.who_starts = "no"
        self.assertEqual(self.game.who_starts, "no")

    def test_main_who_value_error(self):
        """Tests if function raises value error for wrong input word."""
        self.game = GameLoop()
        self.game.who_starts = "n"
        self.assertRaises(ValueError, self.game.main())

    def test_main_red(self):
        self.game = GameLoop()
        self.game.players_color = "red"
        self.assertEqual(self.game.players_color, "red")

    def test_main_red(self):
        self.game = GameLoop()
        self.game.players_color = "yellow"
        self.assertEqual(self.game.players_color, "yellow")

    def test_main_color_value_error(self):
        """Tests if function raises value error for wrong input color."""
        self.game = GameLoop()
        self.game.players_color = "5"
        self.assertRaises(ValueError, self.game.players_color)

    