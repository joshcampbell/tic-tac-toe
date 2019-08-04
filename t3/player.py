from game import Game
from game import default_state

from exceptions import InvalidPlayerException

def first_player(state):
  return state["players"][0]

# FIXME uncovered
def second_player(state):
  return state["players"][1]

class Player:
  def __init__(self,game):
    self.game = game
    self.verify()

  def verify(self):
    assert len(self.game.state["players"]) is 2
    for player in self.game.state["players"]:
      assert isinstance(player, dict), "%s"%type(player)
      # use the default game state as a canonical list of player attributes
      # (initially, "symbol" and "name")
      assert player.keys() == first_player(default_state).keys(), \
        "expected %s, got %s"%(player.keys(),first_player(default_state).keys())

  def get_players(self):
    return self.game.state["players"]

  def valid_symbols(self):
    return map(lambda x: x["symbol"], self.get_players())

  def get_opponent_symbol(self,symbol):
    symbols = self.valid_symbols()
    symbols.remove(symbol)
    return symbols[0]

  def validate_symbol(self,symbol):
    symbols = self.valid_symbols()
    if symbol not in symbols:
      # FIXME uncovered
      raise InvalidPlayerException("Symbol '%s' not in game (valid ones are '%s')"%(symbol,symbols))

  # FIXME uncovered
  def get_active_player(self):
    return self.player_from_symbol(self.get_active_symbol())

  def get_active_symbol(self):
    return self.game.state["active_player"] 

  # FIXME uncovered
  def ordinality(self,player):
    return self.get_players().index(player) + 1

  def player_from_symbol(self,symbol):
    self.validate_symbol(symbol)
    for player in self.get_players():
      if player["symbol"] == symbol:
        return player

  def switch_active(self):
    self.game.state["active_player"] = self.get_opponent_symbol(self.get_active_symbol())
