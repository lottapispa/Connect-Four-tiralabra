import unittest
import math
from minimax import Minimax
from gamestatus import GameStatus
from gamerack import GameRack
from gameloop import GameLoop
from score import Score


class TestGameLoop(unittest.TestCase):
    """Tests class minimax."""

    def setUp(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.minimax = Minimax(self.gamerack, self.gamestatus, self.gameloop.score)
        self.gamestatus.gamerack = self.gamerack

    def minimax_zero_depth(self):
        """Tests if function returns correct value, when depth is 0."""
        self.depth = 0
        self.gameloop.minimax.gamestatus.status = 1
        self.assertEqual(self.gameloop.minimax.minimax(
            self.gamerack.rack, self.depth, -math.inf, math.inf, True), 1)
        #self.gamestatus.status, self.score.score_for_moves(rack, self.gamerack.ai_color), self.score.score_for_moves(rack, self.gamerack.players_color)

    def minimax_true(self):
        self.depth = 10
        self.assertEqual(self.gameloop.minimax.minimax(
            self.gamerack.rack, self.depth, -math.inf, math.inf, True), -math.inf)

    def minimax_false(self):
        self.depth = 10
        self.assertEqual(self.gameloop.minimax.minimax(
            self.gamerack.rack, self.depth, -math.inf, math.inf, False), math.inf)

    def choose_best_move(self):
        self.game = GameLoop()
        self.game.score = Score(self.game.gamerack, self.game.gamestatus)
        self.game.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, "Y", 0, 0, 0, 0, 0], [0, "Y", "R", "R", 0, 0, 0], [0, "Y", "R", "R", "Y", 0, 0]]
        self.game.gamerack.players_color = "Y"
        self.game.gamerack.ai_color = "R"
        self.assertEqual(self.game.score.choose_best_move(
            self.game.gamerack.rack, self.game.gamerack.ai_color), [2, 1])