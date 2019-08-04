import unittest

from t3.game import Game
from t3.player import Player
from t3.moves import Moves

class TestPlayer(unittest.TestCase):
  
  def test_update_symbol(self):
    game = Game({ "players": [ { "symbol": "X", "name": "X"},
                {"symbol": "Y", "name": "Y"}] })
    player = Player(game)
   
  def test_one_player_raises_exception(self):
    game = Game({ "players": [ {"symbol": "Y", "name":"Y"}] })  
    self.assertRaises(Exception, Player, game)

  def test_missing_name_raises_exception(self):
    game = Game({ "players": [ { "symbol": "X"}, {"symbol": "Y",}] })
    self.assertRaises(Exception, Player, game)

  def test_valid_symbols_is_a_set(self):
    symbols = Player(Game()).valid_symbols()
    self.assertIsInstance(symbols,list)

  def test_default_valid_symbols(self):
    game = Game()
    player = Player(game)
    self.assertEqual(set(player.valid_symbols()),{"X","O"})

  def test_nondefault_valid_symbols(self):
    game = Game({ "players": [ { "symbol": "B", "name": "B"}, \
                {"symbol": "A", "name": "A"}] })
    player = Player(game)
    self.assertEqual(set(player.valid_symbols()),{"A","B"})

  def test_starting_player_is_valid(self):
    game = Game({ "players": [ { "symbol": "B", "name": "B"}, \
                {"symbol": "A", "name": "A"}] })
    player = Player(game)
    self.assertIn(player.get_active_symbol(),player.valid_symbols())

  def test_get_opponent_symbol(self):
    game = Game()
    player = Player(game)
    symbol = player.get_opponent_symbol("O")
    self.assertEqual(symbol,"X")

  def test_switching_active_player(self):
    game = Game()
    player = Player(game)
    self.assertEqual(player.get_active_symbol(),"X")
    player.switch_active()
    self.assertEqual(player.get_active_symbol(),"O")

  def test_player_from_symbol(self):
     game = Game()
     player = Player(game)
     Moves(game).perform({
       "player": "X",
       "position": [1,1]
     })
     self.assertEqual(player.player_from_symbol("X"),
                      player.get_players()[0])
