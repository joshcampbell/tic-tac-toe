import unittest

from mock import MagicMock, patch

import t3.curses_prototype.screen as screen

from t3.game_presenter import GamePresenter

class MockScreenTest(unittest.TestCase):

  def setUp(self):
    self.game = GamePresenter()
    self.renderer = screen.RenderState(self.game)
    self.screen = MagicMock()
    self.screen.getmaxyx = MagicMock(return_value=(90,90))
    self.screen.attron = MagicMock()
    self.screen.addstr = MagicMock()

class TestCenteredX(MockScreenTest):

  def test_centers_short_string(self):
    #0123456789
    #    X    
    self.screen.getmaxyx = MagicMock(return_value=(1,10))
    x_pos = screen.centered_x(self.screen, "X")
    self.assertEqual(x_pos, 4)

  def test_centers_longer_string(self):
    #0123456789
    # ABCDEFGH
    self.screen.getmaxyx = MagicMock(return_value=(1,10))
    x_pos = screen.centered_x(self.screen, "ABCDEFGH")
    self.assertEqual(x_pos, 1)

  def test_raises_exception_when_string_wider_than_screen(self):
    self.screen.getmaxyx = MagicMock(return_value=(1,1))
    self.assertRaises(screen.NotEnoughRoomException, screen.centered_x, self.screen, "123")

class TestCenteredY(MockScreenTest):

  def test_centers_simple_string(self):
    #0
    #1 X
    #2
    self.screen.getmaxyx = MagicMock(return_value=(3,1))
    y_pos = screen.centered_y(self.screen, "X")
    self.assertEqual(y_pos, 1)

  def test_centers_tall_string(self):
    #0
    #1
    #2 A
    #3 B
    #4 C
    #5
    #6
    self.screen.getmaxyx = MagicMock(return_value=(7,1))
    y_pos = screen.centered_y(self.screen, "A\nB\nC")
    self.assertEqual(y_pos,2)

  def test_raises_exception_when_string_taller_than_screen(self):
    self.screen.getmaxyx = MagicMock(return_value=(2,1))
    tall_string = "\n\n"
    self.assertRaises(screen.NotEnoughRoomException, screen.centered_y, self.screen, tall_string)

@patch("curses.color_pair")
class TestDrawGameBoard(MockScreenTest):

  def test_number_of_characters_drawn(self, color_pair):
    screen.draw_game_board(self.game, self.renderer, self.screen)
    area = self.renderer.total_board_size * self.renderer.total_board_size
    print self.screen.addstr.call_args_list
    self.assertEqual(self.screen.addstr.call_count, area)
