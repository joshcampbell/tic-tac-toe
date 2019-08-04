from game import Game
from player import Player
from board import Board
from moves import Moves
from victory import Victory

BOARD_TEMPLATE = """
%s|%s|%s
-----------
%s|%s|%s
-----------
%s|%s|%s"""

class GamePresenter:

  # FIXME this class does far too many things

  def __init__(self, game=None):
    if game == None:
      self.game = Game()
    else:
      self.game = game
    self.player = Player(self.game)
    self.players = self.player.get_players()
    self.board = Board(self.game)
    self.moves = Moves(self.game)
    self.victory = Victory(self.game)

  def player_one(self):
    return self.player.get_players()[0]

  def player_one_symbol(self):
    return self.player_one()["symbol"]

  # FIXME uncovered
  def player_two(self):
    return self.player.get_players()[1]

  # FIXME uncovered
  def player_two_symbol(self):
    return self.player_two()["symbol"]

  # FIXME uncovered
  def player_at(self,x,y):
    return self.moves.player_at([x,y])

  # FIXME uncovered
  def board_size(self):
    return self.board.get_size()

  def move(self,x,y,symbol):
    self.moves.perform({
      "player": symbol,
      "position": [x,y]
    })
    self.change_player()

  # FIXME uncovered
  def symbol_at(self,x,y):
    return self.moves.symbol_at([x,y])

  # FIXME uncovered
  def ordinality(self,player):
    return self.player.ordinality(player)

  #FIXME uncovered
  def active_player(self):
    return self.player.get_active_player()

  def active_symbol(self):
    return self.player.get_active_symbol()

  def change_player(self):
    self.player.switch_active()

  # FIXME uncovered
  def clone(self):
    return GamePresenter(self.game.clone())

  def is_draw(self):
    return self.victory.is_impossible()

  def winner(self):
    if self.victory.is_present():
      return self.victory.winning_symbol()
    return None

  # FIXME uncovered
  def is_over(self):
    return self.is_draw() or self.winner() != None

  def dump_board_state(self):
    symbols = []
    for pos in self.board.positions():
      symbol = self.moves.symbol_at(pos)
      if symbol is None:
        symbol = " "
      symbols.append(symbol)
    return BOARD_TEMPLATE % tuple(symbols)
