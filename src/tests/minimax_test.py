import unittest
import math
import time
from gameloop import GameLoop


class TestMinimax(unittest.TestCase):
    """Tests class Minimax."""

    def setUp(self):
        self.game = GameLoop()

    def test_minimax(self):
        """Tests function minimax."""
        self.game = GameLoop()
        self.game.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, "Y", "R", "Y", 0, 0, 0]]
        self.game.gamerack.players_color = "Y"
        self.game.gamerack.ai_color = "R"
        self.assertEqual(self.game.minimax.minimax(
            self.game.rack, 2, -math.inf, math.inf, True), ([4, 2], 0))

    def test_minimax_block_three(self):
        """Tests function minimax."""
        self.game = GameLoop()
        self.game.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, "R", "R", 0, 0], [0, "Y", 0, "Y", "Y", 0, 0]]
        self.game.gamerack.players_color = "Y"
        self.game.gamerack.ai_color = "R"
        self.assertEqual(self.game.minimax.minimax(
            self.game.rack, 2, -math.inf, math.inf, True), ([5, 2], -50))

    def test_minimax_win(self):
        """Tests function minimax."""
        self.game = GameLoop()
        self.game.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, "Y", "R", "R", "R", 0], [0, "Y", "Y", "Y", "R", "Y", "Y"]]
        self.game.gamerack.players_color = "Y"
        self.game.gamerack.ai_color = "R"
        self.assertEqual(self.game.minimax.minimax(
            self.game.rack, 2, -math.inf, math.inf, True), ([4, 6], 28))
