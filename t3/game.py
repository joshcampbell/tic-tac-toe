from copy import deepcopy

default_state = { 
  "board": {
    "size": 3
  },
  "moves": [
  ],
  "players": [
    {
      "symbol": "X",  
      "name": "Alphonse"
    },
    {
      "symbol": "O",  
      "name": "Beatrice"
    }
  ],
  "active_player": "Unset"
}

def verify(state):
  assert set(state.keys()) == set(default_state.keys())

class Game:
  """
  Represents a single session of tic-tac-toe.
  Wraps a dict representing the game state.
  """

  def __init__(self,state={}):
    self.state = deepcopy(default_state) #TODO is this expensive?
    self.state.update(state)
    verify(self.state)
    # FIXME magic string
    if self.state["active_player"] == "Unset":
      self.state["active_player"] = self.state["players"][0]["symbol"]

  def clone(self, delta={}):
    new_state = deepcopy(self.state)
    new_state.update(delta)
    return Game(new_state)
