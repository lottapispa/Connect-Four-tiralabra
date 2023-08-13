import unittest
from gamestatus import GameStatus
from gamerack import GameRack
from gameloop import GameLoop

class TestGameLoop(unittest.TestCase):
    """Tests class score."""

    def setUp(self):
        self.gameloop = GameLoop()
        self.gamerack = GameRack()
        self.gamestatus = GameStatus(self.gamerack)