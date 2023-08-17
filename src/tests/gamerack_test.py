import unittest
from unittest.mock import patch
from gamerack import GameRack


class TestGameRack(unittest.TestCase):
    """Tests class gamerack."""

    def setUp(self):
        pass

    def test_correct_rack_in_the_beginning(self):
        self.gamerack = GameRack()
        self.rack = self.gamerack.rack
        self.assertEqual(self.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece_wrong_input_color(self):
        """Tests if function raises value error for wrong input color and that the rack doesn't change."""
        self.gamerack = GameRack()
        self.rack = self.gamerack.rack
        self.assertRaises(ValueError, self.gamerack.insert_piece, self.rack, 2, 3, "b")
        self.assertEqual(self.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece_wrong_input_row(self):
        """Tests if function raises value error for wrong input row and that the rack doesn't change."""
        self.gamerack = GameRack()
        self.rack = self.gamerack.rack
        self.assertRaises(
            ValueError, self.gamerack.insert_piece, self.rack, 7, 3, "R")
        self.assertEqual(self.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece_wrong_input_column(self):
        """Tests if function raises value error for wrong input column and that the rack doesn't change."""
        self.gamerack = GameRack()
        self.rack = self.gamerack.rack
        self.assertRaises(
            ValueError, self.gamerack.insert_piece, self.rack, 5, 0, "R")
        self.assertEqual(self.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

    def test_insert_piece(self):
        """Tests if the rack changes correctly."""
        self.gamerack = GameRack()
        self.rack = self.gamerack.rack
        self.gamerack.insert_piece(self.rack, 6, 4, "R")
        self.assertEqual(self.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, "R", 0, 0, 0]])

    def test_insert_piece_wrong_input_spot_taken(self):
        """Tests if function raises value error for wrong input (spot already taken) and that the rack doesn't change."""
        self.gamerack = GameRack()
        self.rack = self.gamerack.rack
        self.gamerack.insert_piece(self.rack, 6, 4, "R")
        self.assertRaises(
            ValueError, self.gamerack.insert_piece, self.rack, 6, 4, "Y")
        self.assertEqual(self.rack, [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [
                         0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, "R", 0, 0, 0]])

    def test_next_move(self):
        self.gamerack = GameRack()
        self.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, "Y", 0, 0, 0, 0], [0, 0, "R", 0, 0, 0, 0], [0, 0, "R", "Y", 0, 0, 0]]
        self.assertEqual(self.gamerack.next_move(self.gamerack.rack,), [[5,0],[5,1],[2,2],[4,3],[5,4],[5,5],[5,6]])
        self.assertEqual(self.gamerack.possible_moves, [[5,0],[5,1],[2,2],[4,3],[5,4],[5,5],[5,6]])
    
    def test_is_valid_row_true(self):
        self.gamerack = GameRack()
        self.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(self.gamerack.is_valid(6, None))

    def test_is_valid_row_false(self):
        self.gamerack = GameRack()
        self.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(self.gamerack.is_valid(5, None))

    def test_is_valid_column_true(self):
        self.gamerack = GameRack()
        self.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, "Y", 0, 0, 0]]
        self.assertTrue(self.gamerack.is_valid(6, 7))

    def test_is_valid_column_false(self):
        self.gamerack = GameRack()
        self.gamerack.rack = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, "Y", 0, 0, 0]]
        self.assertFalse(self.gamerack.is_valid(6, 4))

    @patch('builtins.print')
    def test_print_rack(self, mock_print):
        self.gamerack = GameRack()
        self.gamerack.print_rack()
        mock_print.assert_called_with([0, 0, 0, 0, 0, 0, 0])
