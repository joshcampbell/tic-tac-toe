from game import Game
from board import Board

class ThroughLine():

  def __init__(self,game):
    self.game = game
    self.range = Board(game).get_valid_indices()

  def all(self):
    all = self.rows()
    all += self.columns()
    all += self.diagonals()
    return all

  def rows(self):
    return [[[row,col] for col in self.range] 
                       for row in self.range]

  def columns(self):
    return [[[row,col] for row in self.range]
                       for col in self.range]

  def diagonals(self):
    return [[[column, diagonal[column-1]] for column in self.range ] 
            for diagonal in [list(reversed(self.range)),self.range]]
