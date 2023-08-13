import unittest
from minimax import Minimax
from gamestatus import GameStatus
from gamerack import GameRack
from gameloop import GameLoop
import math

class TestGameLoop(unittest.TestCase):
    """Tests class minimax."""

    def setUp(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.minimax = Minimax(self.gamerack, self.gamestatus)
        self.gamestatus.gamerack = self.gamerack

    def test_minimax_zero_depth(self):
        """Tests if function returns correct value, when depth is 0."""
        self.depth = 0
        self.gameloop.minimax.gamestatus.status = 1
        self.assertEqual(self.gameloop.minimax.minimax(self.gamerack.rack, self.depth, -math.inf, math.inf, True), 1)

    def minimax_true(self):
        self.depth = 6
        #self.gamerack.rack = 
        self.assertEqual(self.gameloop.minimax.minimax(self.gamerack.rack, self.depth, -math.inf, math.inf, True), -math.inf)

    def minimax_false(self):
        self.depth = 6
        #self.gamerack.rack = 
        self.assertEqual(self.gameloop.minimax.minimax(self.gamerack.rack, self.depth, -math.inf, math.inf, False), math.inf)
        