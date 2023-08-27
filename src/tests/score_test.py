import unittest
from score import Score
from gameloop import GameLoop


class TestGameLoop(unittest.TestCase):
    """Tests class score."""

    def setUp(self):
        self.game = GameLoop()

    def test_winning_move_yes(self):
        """Tests if function winning_move returns correct winning move row and column as list."""
        self.game = GameLoop()
        self.game.score = Score(self.game.gamerack, self.game.gamestatus)
        self.game.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, "Y", 0, 0, 0, 0, 0], [0, "Y", "R", "R", 0, 0, 0], [0, "Y", "R", "R", "Y", 0, 0]]
        self.assertEqual(self.game.score.winning_move("Y"), [2, 1])

    def test_winning_move_false(self):
        """Tests if function winning_move returns false when no winning move."""
        self.game = GameLoop()
        self.game.score = Score(self.game.gamerack, self.game.gamestatus)
        self.game.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, "Y", "R", "R", 0, 0, 0], [0, "Y", "R", "R", "Y", 0, 0]]
        self.assertFalse(self.game.score.winning_move("Y"))

    def test_score_for_moves_player(self):
        self.game = GameLoop()
        self.game.score = Score(self.game.gamerack, self.game.gamestatus)
        self.game.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [
            0, "Y", 0, 0, 0, 0, 0], [0, "Y", "R", "R", 0, 0, 0], [0, "Y", "R", "R", "Y", 0, 0]]
        self.game.gamerack.players_color = "Y"
        self.game.gamerack.ai_color = "R"
        self.assertEqual(self.game.score.score_for_moves(
            self.game.gamerack.rack, self.game.gamerack.players_color), 115)

    def test_score_for_moves_opp(self):
        self.game = GameLoop()
        self.game.score = Score(self.game.gamerack, self.game.gamestatus)
        self.game.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, "Y", "R", 0, 0, 0, 0], [0, "Y", "R", 0, 0, 0, 0], [0, "Y", "R", "R", "Y", 0, 0]]
        self.game.gamerack.players_color = "Y"
        self.game.gamerack.ai_color = "R"
        self.assertEqual(self.game.score.score_for_moves(
            self.game.gamerack.rack, self.game.gamerack.ai_color), -65)
