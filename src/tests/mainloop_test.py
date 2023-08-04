import unittest
from mainloop import GameLoop

class TestGameLoop(unittest.TestCase):
    """Tests class gameloop."""

    def setUp(self):
        self.turn = GameLoop().turn

    def test_main_value_error(self):
        """Tests if function raises value error for wrong input word."""
        self.gameloop = GameLoop()
        who_starts = self.who_starts
        who_starts = "n"
        self.assertEqual(who_starts, "n")
        self.assertRaises(ValueError, who_starts = "n")

    def test_main_value_error_color(self):
        """Tests if function raises value error for wrong input color."""
        self.gameloop = GameLoop()
        who_starts = self.who_starts
        who_starts = "r"
        self.assertEqual(who_starts, "r")
        self.assertRaises(ValueError, players_color = "r")

    