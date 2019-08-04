from copy import copy

from board import Board
from player import Player

from exceptions import ImpossibleMoveException
from exceptions import NoMovesToUndoException

# FIXME It's less than ideal that "perform" takes a dict as its argument,
#       rather than named parameters.

class Moves:

  def __init__(self,game):
    self.game = game
    self.board = Board(game)
    self.player = Player(game)

  # FIXME uncovered
  def validate(self,move):
   assert self.is_move_well_formed(move), move
   self.board.validate_position(move["position"])
   assert not self.is_position_occupied(move), "%s is occupied"%move["position"]
   return True

  def valid(self,move):
    return self.is_move_well_formed(move) and \
           self.board.is_valid_position(move["position"]) and \
           not self.is_position_occupied(move)

  def perform_all(self,moves):
    for move in moves:
      self.perform(move)

  def perform(self,move):
    if not self.valid(move):
      # FIXME uncovered
      raise ImpossibleMoveException("Move %s is invalid."%move)
    self.player.validate_symbol(move["player"])
    self.game.state["moves"].append(move)

  def get_history(self):
    return self.game.state["moves"]

  def is_occupied(self,position):
    return position in self.get_occupied_positions()

  def get_occupied_positions(self):
    return map(lambda x: x["position"], self.get_history())

  def get_empty_positions(self):
    all_positions = self.board.positions()
    empty_positions = copy(all_positions)
    occupied_positions = self.get_occupied_positions()
    for position in occupied_positions:
      empty_positions.remove(position)
    return empty_positions

  def symbol_at(self,position):
    move = self.move_at(position)
    if move:
      return move["player"]
    return None

  # FIXME uncovered
  def player_at(self,position):
    move = self.move_at(position)
    if move is not None:
      return self.player.player_from_symbol(move["player"])

  # FIXME uncovered
  def undo(self):
    moves = self.game.state["moves"]
    # remove the last Player and AI moves
    if len(moves) > 1:
      moves.remove(moves[-1])
      moves.remove(moves[-1])
    else:
      raise NoMovesToUndoException()

  def move_at(self,position):
    assert self.board.is_valid_position(position)
    for move in self.game.state["moves"]:
      if move["position"] == position:
        return move
    return None

  def is_move_well_formed(self,move):
    return set(move.keys()) == set(["position", "player"]) and \
           isinstance(move["position"],list) and \
             (isinstance(move["player"],str) or \
              isinstance(move["player"],unicode))

  def is_position_occupied(self,move):
    return move["position"] in self.get_occupied_positions()
