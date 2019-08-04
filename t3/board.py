import itertools

class Board:

  def __init__(self,game):
    self.game = game

  def get_size(self):
    return self.game.state["board"]["size"]

  def get_valid_indices(self):
    return range(1,self.get_size()+1)

  def positions(self):
    """
    Enumerate all of the Board's positions as a list of lists 
      (for JSON reasons)
    """
    positions = []
    for row in self.get_valid_indices():
      for col in self.get_valid_indices():
        positions.append([row,col])
    return positions

  def corners(self):
    max_index = self.get_valid_indices()[-1]
    extremes = [1,max_index]
    return filter(lambda pos: pos[0] in extremes \
                              and pos[1] in extremes,
                  self.positions())

  # FIXME DRY, possibly factor out class or module
  def is_valid_position(self,position):
    return self.is_position_well_formed(position) and \
           self.is_within_bounds(position)

  # FIXME uncovered
  def validate_position(self,position):
    assert self.is_position_well_formed(position), "malformed position: %s" % position
    assert self.is_within_bounds(position), "%s not in %s"%(position,\
                                             self.get_valid_indices())

  def is_within_bounds(self,position):
    return position in self.positions()

  def is_position_well_formed(self,position):
    return isinstance(position[0],int) and \
           isinstance(position[1],int)
