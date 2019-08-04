import unittest

from t3.game import Game
from t3.game_ai_presenter import GameAIPresenter

class TestGameAIPresenter(unittest.TestCase):

        def test_next_states_on_empty_board(self):
                game = Game()
                subject = GameAIPresenter(game)
                self.assertEqual(len(subject.potential_next_states()),9)

        def test_next_states_on_nearly_full_board(self):
                game = Game()
                subject = GameAIPresenter(game)
                subject.move(1,1,"O")
                self.assertEqual(len(subject.potential_next_states()),8)
                subject.move(2,2,"X")
                self.assertEqual(len(subject.potential_next_states()),7)
                subject.move(3,3,"O")
                self.assertEqual(len(subject.potential_next_states()),6)
                subject.move(1,2,"X")
                self.assertEqual(len(subject.potential_next_states()),5)
                subject.move(1,3,"O")
                self.assertEqual(len(subject.potential_next_states()),4)
