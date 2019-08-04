import unittest

from t3.game import Game
from t3.player import Player

class TestSanity(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_empty_constructor(self):
        assert isinstance(self.game,Game)

    def test_game_state_exists(self):
        assert isinstance(self.game.state,dict)

    def test_game_tracks_board(self):
        assert isinstance(self.game.state["board"],dict)

    def test_game_tracks_board_side_length(self):
        assert isinstance(self.game.state["board"]["size"],int)

    def test_game_tracks_moves(self):
        assert isinstance(self.game.state["moves"],list)

    def test_game_tracks_players(self):
        assert isinstance(self.game.state["players"],list)

    def test_game_tracks_active_player(self):
         assert isinstance(self.game.state["active_player"],str)
