import unittest
from score import Score
from gameloop import GameLoop


class TestScore(unittest.TestCase):
    """Tests class score."""

    def setUp(self):
        self.game = GameLoop()

    def test_score_for_moves_player(self):
        self.game = GameLoop()
        self.game.score = Score(self.game.gamerack, self.game.gamestatus)
        self.game.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [
            0, "Y", 0, 0, 0, 0, 0], [0, "Y", "R", "R", 0, 0, 0], [0, "Y", "R", "R", "Y", 0, 0]]
        self.game.gamerack.players_color = "Y"
        self.game.gamerack.ai_color = "R"
        self.assertEqual(self.game.score.score_for_moves(
            self.game.gamerack.rack, self.game.gamerack.players_color), 94)

    def test_score_for_moves_opp(self):
        self.game = GameLoop()
        self.game.score = Score(self.game.gamerack, self.game.gamestatus)
        self.game.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, "Y", "R", 0, 0, 0, 0], [0, "Y", "R", 0, 0, 0, 0], [0, "Y", "R", "R", "Y", 0, 0]]
        self.game.gamerack.players_color = "Y"
        self.game.gamerack.ai_color = "R"
        self.assertEqual(self.game.score.score_for_moves(
            self.game.gamerack.rack, self.game.gamerack.ai_color), -61)
