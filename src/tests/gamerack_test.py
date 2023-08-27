import unittest
from unittest.mock import patch
from gamerack import GameRack
from gameloop import GameLoop


class TestGameRack(unittest.TestCase):
    """Tests class gamerack."""

    def setUp(self):
        pass

    def test_correct_rack_in_the_beginning(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack(self.gameloop.rack)
        self.assertEqual(self.gameloop.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece_wrong_input_color(self):
        """Tests if function raises value error for wrong input color and that the rack doesn't change."""
        self.gameloop = GameLoop()
        self.gamerack = GameRack(self.gameloop.rack)
        self.assertRaises(
            ValueError, self.gamerack.insert_piece, self.gameloop.rack, 5, 3, "b")
        self.assertEqual(self.gameloop.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece_wrong_input_row(self):
        """Tests if function raises value error for wrong input row and that the rack doesn't change."""
        self.gameloop = GameLoop()
        self.gamerack = GameRack(self.gameloop.rack)
        self.assertRaises(
            ValueError, self.gamerack.insert_piece, self.gameloop.rack, 7, 3, "R")
        self.assertEqual(self.gameloop.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece_wrong_input_column(self):
        """Tests if function raises value error for wrong input column and that the rack doesn't change."""
        self.gameloop = GameLoop()
        self.gamerack = GameRack(self.gameloop.rack)
        self.assertRaises(
            ValueError, self.gamerack.insert_piece, self.gameloop.rack, 5, 7, "R")
        self.assertEqual(self.gameloop.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece(self):
        """Tests if the rack changes correctly."""
        self.gameloop = GameLoop()
        self.gamerack = GameRack(self.gameloop.rack)
        self.gamerack.insert_piece(self.gameloop.rack, 5, 3, "R")
        self.assertEqual(self.gameloop.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, "R", 0, 0, 0]])

    def insert_piece_wrong_input_spot_taken(self):
        """Tests if function raises value error for wrong input (spot already taken) and that the rack doesn't change."""
        self.gameloop = GameLoop()
        self.gamerack = GameRack(self.gameloop.rack)
        self.gamerack.insert_piece(self.gameloop.rack, 5, 3, "R")
        self.assertRaises(
            ValueError, self.gamerack.insert_piece, self.gameloop.rack, 5, 3, "Y")
        self.assertEqual(self.gameloop.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, "R", 0, 0, 0]])

    def test_next_move_full(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack(self.gameloop.rack)
        self.gameloop.rack = [["Y", "R", "Y", "R", "Y", "R", "Y"], ["R", "Y", "R", "Y", "R", "Y", "R"], ["R", "Y", "R", "Y", "R", "Y", "R"], [
            "Y", "R", "Y", "R", "Y", "R", "Y"], ["Y", "R", "Y", "R", "Y", "R", "Y"], ["R", "Y", "R", "Y", "R", "Y", "R"]]
        self.assertEqual(self.gamerack.next_move(self.gameloop.rack,), [])
        self.assertEqual(self.gamerack.possible_moves, [])

    def test_next_move(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack(self.gameloop.rack)
        self.gameloop.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, "Y", 0, 0, 0, 0], [0, 0, "R", 0, 0, 0, 0], [0, 0, "R", "Y", 0, 0, 0]]
        self.assertEqual(self.gamerack.next_move(self.gameloop.rack,), [
                         [5, 0], [5, 1], [2, 2], [4, 3], [5, 4], [5, 5], [5, 6]])
        self.assertEqual(self.gamerack.possible_moves, [
                         [5, 0], [5, 1], [2, 2], [4, 3], [5, 4], [5, 5], [5, 6]])

    def test_is_valid_true(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack(self.gameloop.rack)
        self.gameloop.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.gamerack.is_valid(4), 5)

    def is_valid_false(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack(self.gameloop.rack)
        self.gameloop.rack = [["Y", "R", "Y", "R", "Y", "R", "Y"], ["R", "Y", "R", "Y", "R", "Y", "R"], ["R", "Y", "R", "Y", "R", "Y", "R"], [
            "Y", "R", "Y", "R", "Y", "R", "Y"], ["Y", "R", "Y", "R", "Y", "R", "Y"], ["R", "Y", "R", "Y", "R", "Y", "R"]]
        self.assertFalse(self.gamerack.is_valid(0))

    @patch('builtins.print')
    def test_print_rack(self, mock_print):
        self.gameloop = GameLoop()
        self.gamerack = GameRack(self.gameloop.rack)
        self.gamerack.print_rack()
        mock_print.assert_called_with([0, 0, 0, 0, 0, 0, 0])
