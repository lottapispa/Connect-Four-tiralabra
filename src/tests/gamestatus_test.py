import unittest
from gamestatus import GameStatus


class TestGameStatus(unittest.TestCase):
    """Tests class gamestatus."""

    def setUp(self):
        self.rows = GameStatus().rows
        self.columns = GameStatus().columns

    def is_game_over_tie(self):
        self.gamestatus = GameStatus()
        self.gamestatus.rack = [["Y", "R", "Y", "R", "Y", "R", "Y"], ["R", "Y", "R", "Y", "R", "Y", "R"], ["R", "Y", "R", "Y", "R", "Y", "R"], [
            "Y", "R", "Y", "R", "Y", "R", "Y"], ["Y", "R", "Y", "R", "Y", "R", "Y"], ["R", "Y", "R", "Y", "R", "Y", "R"]]
        self.gamestatus.is_game_over()
        self.assertTrue(self.gamestatus.over)
        self.assertTrue(self.gamestatus.tie)

    def test_is_game_over_true(self):
        self.gamestatus = GameStatus()
        self.gamestatus.rack = [[0, "R", "R", "R", "R", 0, 0], [0, "Y", 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.gamestatus.over
        self.gamestatus.is_game_over()
        self.assertTrue(self.gamestatus.over)

    def test_is_game_over_false(self):
        self.gamestatus = GameStatus()
        self.rack = self.gamestatus.rack
        self.over = self.gamestatus.over
        self.gamestatus.is_game_over()
        self.assertFalse(self.over)

    def test_check_for_win_hor_true(self):
        self.gamestatus = GameStatus()
        self.gamestatus.rack = [[0, "R", "R", "R", "R", 0, 0], [0, "Y", 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_hor())

    def test_check_for_win_hor_false(self):
        self.gamestatus = GameStatus()
        self.gamestatus.rack = [[0, "R", "Y", "R", "R", 0, 0], [0, "Y", 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(self.gamestatus.check_for_win_hor())

    def test_check_for_win_ver_true(self):
        self.gamestatus = GameStatus()
        self.gamestatus.rack = [[0, "R", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [
            0, "Y", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_ver())

    def test_check_for_win_ver_false(self):
        self.gamestatus = GameStatus()
        self.gamestatus.rack = [[0, "R", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [
            0, "Y", 0, 0, 0, 0, 0], [0, "R", 0, 0, 0, 0, 0], [0, "Y", 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(self.gamestatus.check_for_win_ver())

    def test_check_for_win_dia_true_R(self):
        self.gamestatus = GameStatus()
        self.gamestatus.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, "R", 0, 0, 0, 0], [0, 0, 0, "R", 0, 0, 0], [
            0, 0, 0, 0, "R", 0, 0], [0, 0, 0, 0, 0, "R", 0], [0, 0, "Y", 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_dia())

    def test_check_for_win_dia_true_Y(self):
        self.gamestatus = GameStatus()
        self.gamestatus.rack = [["R", 0, 0, 0, 0, 0, 0], [0, 0, "Y", 0, 0, 0, 0], ["R", 0, 0, "Y", 0, 0, 0], [
            0, 0, 0, 0, "Y", 0, 0], [0, 0, 0, 0, 0, "Y", 0], [0, 0, "R", 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_dia())

    def test_check_for_win_dia_true_R_other_way(self):
        self.gamestatus = GameStatus()
        self.gamestatus.rack = [[0, 0, 0, "Y", 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, "R", 0, 0, 0], [
            0, 0, "R", 0, 0, 0, 0], [0, "R", 0, 0, 0, "Y", 0], ["R", 0, "Y", 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_dia())

    def test_check_for_win_dia_true_Y_other_way(self):
        self.gamestatus = GameStatus()
        self.gamestatus.rack = [[0, 0, 0, "R", 0, 0, 0], [0, 0, 0, 0, "Y", 0, 0], [0, 0, 0, "Y", 0, 0, 0], [
            0, 0, "Y", 0, 0, 0, 0], [0, "Y", 0, 0, 0, "R", 0], [0, 0, "R", 0, 0, 0, 0]]
        self.assertTrue(self.gamestatus.check_for_win_dia())

    def test_check_for_win_dia_false(self):
        self.gamestatus = GameStatus()
        self.gamestatus.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, "R", 0, 0, 0, 0], [0, 0, 0, "R", 0, 0, 0], [
            0, 0, 0, 0, "Y", 0, 0], [0, 0, 0, 0, 0, "R", 0], [0, 0, "Y", 0, 0, 0, 0]]
        self.assertFalse(self.gamestatus.check_for_win_dia())
