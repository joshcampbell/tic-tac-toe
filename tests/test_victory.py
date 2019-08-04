import unittest

from t3.game import Game
from t3.victory import Victory
from t3.through_line import ThroughLine
from t3.moves import Moves

class TestVictory(unittest.TestCase):
  
  def test_default_game_state_is_not_victorious(self):
    game = Game()
    victory = Victory(game)
    assert not victory.is_present()

  def test_default_game_state_has_no_winner(self):
    game = Game()
    victory = Victory(game)
    self.assertEqual(victory.winning_symbol(),None)

  def test_victory_by_filled_row(self):
    game = Game()
    victory = Victory(game)
    moves = Moves(game)
    # create a winning line consisting of the top row
    winning_line = [[1,1],[1,2],[1,3]]
    winning_moves = [{"player":"X","position":position} for position in winning_line]
    moves.perform_all(winning_moves)
    assert victory.is_present()

  def test_victory_has_winner(self):
    game = Game()
    victory = Victory(game)
    moves = Moves(game)
    # create a winning line consisting of the top row
    winning_line = ThroughLine(game).rows()[0]
    winning_moves = [{"player":"X","position":position} for position in winning_line]
    moves.perform_all(winning_moves)
    self.assertEquals(victory.winning_symbol(),"X")

  def test_second_row_victory(self):
    game = Game()
    victory = Victory(game)
    moves = Moves(game)
    winning_line = [[2,1],[2,2],[2,3]]
    winning_moves = [{"player":"X","position":position} for position in winning_line]
    moves.perform_all(winning_moves)
    self.assertEquals(victory.winning_symbol(),"X")
    
  def test_three_moves_required(self):
    game = Game()
    moves = Moves(game)
    victory = Victory(game)
    # create a winning line consisting of the top row
    winning_line = ThroughLine(game).rows()[0]
    winning_moves = [{"player":"X","position":position} for position in winning_line]
    for move in winning_moves:
      moves.perform(move) 
      assert not victory.is_present() or move["position"] == [1,3]

  def test_vertical_victory(self):
    game = Game()
    victory = Victory(game)
    moves = Moves(game)
    winning_line = [[1,1],[2,1],[3,1]]
    winning_moves = [{"player":"X","position":position} for position in winning_line]
    moves.perform_all(winning_moves)
    assert victory.is_present()

  def test_diagonal_victory(self):
    game = Game()
    victory = Victory(game)
    moves = Moves(game)
    winning_line = [[1,1],[2,2],[3,3]]
    winning_moves = [{"player":"X","position":position} for position in winning_line]
    moves.perform_all(winning_moves)
    assert victory.is_present()
