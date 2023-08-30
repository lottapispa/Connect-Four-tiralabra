import unittest
import math
from minimax import Minimax
from gamestatus import GameStatus
from gamerack import GameRack
from gameloop import GameLoop
from score import Score


class TestMinimax(unittest.TestCase):
    """Tests class minimax."""

    def setUp(self):
        self.gameloop = GameLoop()

    def test_choose_best_move(self):
        """Tests class Minimax."""
        self.game = GameLoop()
        self.game.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, "R", 0, "R", "R", 0, 0], [0, "Y", 0, "Y", "Y", 0, 0]]
        self.game.gamerack.players_color = "Y"
        self.game.gamerack.ai_color = "R"
        self.assertEqual(self.game.minimax.choose_best_move(
            self.game.rack, self.game.gamerack.ai_color), [5, 2])
