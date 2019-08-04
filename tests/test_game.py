import unittest

from t3.game import Game
from t3.game import default_state

class TestGame(unittest.TestCase):

    def test_empty_constructor(self):
      """
      Game's constructor takes a single, optional parameter: a dict containing
      a complete or partial game state, which is merged with a copy of the 
      default state to produce the instance's starting state.
      """
      subject = Game()
      modified_default = default_state
      modified_default.update({"active_player":"X"})
      self.assertEqual(subject.state, modified_default) 

    def test_update_board_size(self):
      subject = Game({"board": { "size": 5 }})
      self.assertEqual(subject.state["board"]["size"],5)

    def test_unknown_key_exception(self):
      with self.assertRaises(Exception):
        Game({ "badkey": [] })

    def test_clone_returns_copy(self):
      subject = Game()
      clone = subject.clone()
      assert subject is not clone
      assert subject.state is not clone.state
