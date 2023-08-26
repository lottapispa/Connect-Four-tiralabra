import unittest
from gamestatus import GameStatus
from gameloop import GameLoop
from gamerack import GameRack


class TestGameStatus(unittest.TestCase):
    """Tests class gamestatus."""

    def setUp(self):
        self.gamerack = GameRack()
        self.rows = GameStatus(self.gamerack).rows
        self.columns = GameStatus(self.gamerack).columns

    def test_is_game_over_tie(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.rack = [["Y", "R", "Y", "R", "Y", "R", "Y"], ["R", "Y", "R", "Y", "R", "Y", "R"], ["R", "Y", "R", "Y", "R", "Y", "R"], [
            "Y", "R", "Y", "R", "Y", "R", "Y"], ["Y", "R", "Y", "R", "Y", "R", "Y"], ["R", "Y", "R", "Y", "R", "Y", "R"]]
        # self.gamestatus.is_game_over(self.gamestatus.gamerack.rack)
        self.assertTrue(self.gamestatus.is_game_over(
            self.gamestatus.gamerack.rack))
        self.assertEqual(self.gamestatus.status, 0)

    def test_is_game_over_true_player(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.players_color = "R"
        self.gamestatus.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, "Y", "Y", 0, 0, 0, 0], [0, "Y", "R", "R", "R", "R", 0]]
        self.assertTrue(self.gamestatus.is_game_over(
            self.gamestatus.gamerack.rack))
        self.gamestatus.is_game_over(self.gamestatus.gamerack.rack)
        self.assertEqual(self.gamestatus.status, -100)

    def test_is_game_over_true_ai(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.ai_color = "Y"
        self.gamestatus.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, "Y", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [0, "Y", "R", "R", "R", 0, 0]]
        self.assertTrue(self.gamestatus.is_game_over(
            self.gamestatus.gamerack.rack))
        self.gamestatus.is_game_over(self.gamestatus.gamerack.rack)
        self.assertEqual(self.gamestatus.status, 100)

    def test_is_game_over_false(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.assertFalse(self.gamestatus.is_game_over(
            self.gamestatus.gamerack.rack))
        # self.assertEqual(self.gamestatus.status, None)

    def test_check_for_win_hor_true(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.rack = [[0, "R", "R", "R", "R", 0, 0], [0, "Y", 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_hor(
            self.gamestatus.gamerack.rack))

    def test_check_for_win_hor_false(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.rack = [[0, "R", "Y", "R", "R", 0, 0], [0, "Y", 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(self.gamestatus.check_for_win_hor(
            self.gamestatus.gamerack.rack))

    def test_check_for_win_ver_true(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.rack = [[0, "R", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [
            0, "Y", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_ver(
            self.gamestatus.gamerack.rack))

    def test_check_for_win_ver_false(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.rack = [[0, "R", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [
            0, "Y", 0, 0, 0, 0, 0], [0, "R", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(self.gamestatus.check_for_win_ver(
            self.gamestatus.gamerack.rack))

    def test_check_for_win_dia_true_R(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, "R", 0, 0, 0, 0], [0, 0, 0, "R", 0, 0, 0], [
            0, 0, 0, 0, "R", 0, 0], [0, 0, 0, 0, 0, "R", 0], [0, 0, "Y", 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_dia(
            self.gamestatus.gamerack.rack))

    def test_check_for_win_dia_true_Y(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.rack = [["R", 0, 0, 0, 0, 0, 0], [0, 0, "Y", 0, 0, 0, 0], ["R", 0, 0, "Y", 0, 0, 0], [
            0, 0, 0, 0, "Y", 0, 0], [0, 0, 0, 0, 0, "Y", 0], [0, 0, "R", 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_dia(
            self.gamestatus.gamerack.rack))

    def test_check_for_win_dia_true_R_other_way(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.rack = [[0, 0, 0, "Y", 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, "R", 0, 0, 0], [
            0, 0, "R", 0, 0, 0, 0], [0, "R", 0, 0, 0, "Y", 0], ["R", 0, "Y", 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_dia(
            self.gamestatus.gamerack.rack))

    def test_check_for_win_dia_true_Y_other_way(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.rack = [[0, 0, 0, "R", 0, 0, 0], [0, 0, 0, 0, "Y", 0, 0], [0, 0, 0, "Y", 0, 0, 0], [
            0, 0, "Y", 0, 0, 0, 0], [0, "Y", 0, 0, 0, "R", 0], [0, 0, "R", 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_dia(
            self.gamestatus.gamerack.rack))

    def test_check_for_win_dia_false(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)
        self.gamestatus.gamerack = self.gamerack
        self.gamestatus.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, "R", 0, 0, 0, 0], [0, 0, 0, "R", 0, 0, 0], [
            0, 0, 0, 0, "Y", 0, 0], [0, 0, 0, 0, 0, "R", 0], [0, 0, "Y", 0, 0, 0, 0]]
        self.assertFalse(self.gamestatus.check_for_win_dia(
            self.gamestatus.gamerack.rack))
