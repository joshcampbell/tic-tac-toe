import unittest

from t3.game import Game
from t3.moves import Moves
from t3.board import Board

class TestMoves(unittest.TestCase):
  
  def test_mutates_game_state(self):
    game = Game()
    moves = Moves(game)
    assert moves.game is game
    assert moves.game.state is game.state
    moves.perform({"position":[1,1],"player":"X"})
    self.assertEqual(len(game.state["moves"]),1)

  def test_move_must_be_within_board(self):
    game = Game()
    moves = Moves(game)
    move ={ "position": [-1,2], "player":"X"} 
    self.assertRaises(Exception,moves.valid,)

  def test_position_not_occupied_before_moving(self):
    game = Game()
    moves = Moves(game)
    board = Board(game)
    for position in board.positions():
      assert not moves.is_occupied(position) 

  def test_position_occupied_after_moving(self):
    game = Game()
    moves = Moves(game)
    move = { "position": [1,1], "player": "X" }
    moves.perform(move)
    assert moves.is_occupied(move['position'])

  def test_occupied_position_has_player(self):
    game = Game()
    moves = Moves(game)
    move = { "position": [1,1], "player": "X" }
    moves.perform(move)
    self.assertEqual(moves.symbol_at([1,1]), "X")

  def test_empty_positions_list(self):
    game = Game()
    moves = Moves(game)
    self.assertEqual(len(moves.get_empty_positions()), 9)
    move = { "position": [1,1], "player": "X" }
    assert move["position"] not in moves.get_occupied_positions()
    moves.perform(move)
    assert move["position"] not in moves.get_empty_positions()
    self.assertEqual(len(moves.get_empty_positions()), 8)
