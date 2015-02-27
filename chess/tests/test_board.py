import unittest
from chess.board import Board

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_initializes_with_64_squares(self):
        assertEquals(len(self.board), 64)
