import unittest

from t3.game import Game
from t3.board import Board
from t3.through_line import ThroughLine

class TestThroughLine(unittest.TestCase):

  def setUp(self):
    self.game = Game()
    self.subject = ThroughLine(self.game)
    self.board_size = Board(self.game).get_size()

  def test_contains_n_rows(self):
     self.assertEqual(len(self.subject.rows()),self.board_size)

  def test_contains_n_columns(self):
     self.assertEqual(len(self.subject.columns()),self.board_size)

  def test_contains_2_diagonals(self):
     self.assertEqual(len(self.subject.diagonals()), 2)

  def test_contains_n_total_lines(self):
     self.assertEqual(len(self.subject.all()), (self.board_size*2)+2)
