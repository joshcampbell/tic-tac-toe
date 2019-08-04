import unittest

from t3.game import Game
from t3.board import Board

class TestBoard(unittest.TestCase):

  def test_nine_board_positions_by_default(self):
    game = Game()
    board = Board(game)
    self.assertEqual(len(board.positions()), 9)

  def test_board_positions_are_lists(self):
    # they're not tuples because I have a dream of sending game states
    # back and forth as JSON
    positions = Board(Game()).positions()    
    for position in positions:
      self.assertIsInstance(position, list)

  def test_four_corners(self):
    corners = Board(Game()).corners()
    self.assertEqual(len(corners), 4)
