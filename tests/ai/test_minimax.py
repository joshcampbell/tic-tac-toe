import unittest

import sys

from t3.through_line import ThroughLine
from t3.game_ai_presenter import GameAIPresenter

from t3.ai.minimax import Minimax
from t3.ai.minimax import best_moves

class TestNegaMax(unittest.TestCase):

    def setUp(self):
        self.game = GameAIPresenter()
        self.symbol = "X"
        self.other = "O"
        self.negamax = Minimax(self.game,self.symbol)

    def move_self(self,moves):
        for x, y in moves:
            self.game.move(x,y,self.symbol)

    def move_other(self,moves):
        for x, y in moves:
            self.game.move(x,y,self.other)

    def test_negamax_refers_to_game(self):
        self.assertIs(self.negamax.game, self.game)

    def test_moves_to_victory(self):
        self.move_self([(1,1),(2,2)])
        self.move_other([(1,2),(1,3)])
        best_moves = self.negamax.get_best_moves()
        self.assertEqual(best_moves[0][0],(3,3))

    def test_successive_next_states(self):
        pos,future_1 = self.negamax.potential_games()[0]
        child_1 = Minimax(future_1,self.symbol,2)
        pos,future_2 = child_1.potential_games()[0]
        child_2 = Minimax(future_2,self.symbol,2)
        self.assertEqual(len(child_2.potential_games()),7)

    def test_moves_to_avoid_defeat(self):
        # create near defeat
        self.move_other([(1,1),(3,3),(1,3)])
        self.move_self([(3,1),(2,2)])
        self.game.game.state["active_player"] = "X"
        best_moves = self.negamax.get_best_moves()
        self.assertEqual(best_moves[0][0],(1,2))
