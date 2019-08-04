from moves import Moves
from through_line import ThroughLine

class Victory():

  def __init__(self,game):
    self.game = game
    self.moves = Moves(game)
    self.through_line = ThroughLine(game)

  def is_present(self):
    return self.winning_symbol() != None

  def winning_symbol(self): 
    lines = self.through_line.all()
    for line in lines:
      symbols = []
      for position in line:
        symbols.append(self.moves.symbol_at(position))
      if len(set(symbols)) is 1:
        only_symbol = list(set(symbols))[0]
        if only_symbol is not None:
          return only_symbol
    return None

  def is_impossible(self):
    lines = self.through_line.all()
    dead_line_count = 0
    for line in lines:
      symbols = []
      for position in line:
        symbols.append(self.moves.symbol_at(position))
      if len(filter(lambda x: x != None, set(symbols))) is 2:
        dead_line_count += 1
    if dead_line_count is len(lines):
      return True
    else:
      return False
