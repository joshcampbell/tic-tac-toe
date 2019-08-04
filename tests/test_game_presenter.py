import unittest

from t3.game_presenter import GamePresenter

class TestGamePresenter(unittest.TestCase):

    def setUp(self):
        self.subject = GamePresenter()
        self.symbol = self.subject.player_one_symbol()

    def test_initial_empty_board(self):
        board_as_string = self.subject.dump_board_state()
        self.assertEqual(board_as_string[1]," ")

    def test_moving_upper_left(self):
        self.subject.move(1,1,self.symbol)
        board_as_string = self.subject.dump_board_state()
        self.assertEqual(board_as_string[1],self.symbol)

    def test_moving_lower_right(self):
        self.subject.move(3,3,self.symbol)
        board_as_string = self.subject.dump_board_state()
        self.assertEqual(board_as_string[-1],self.symbol)
