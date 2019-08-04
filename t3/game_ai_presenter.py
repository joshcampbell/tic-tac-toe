from moves import Moves
import logging

from game_presenter import GamePresenter

__log = logging.getLogger('ai_presenter')
__log.addHandler(logging.FileHandler('./tmp/ai_presenter.log'))

def log(message):
  # FIXME toggle logging based on configuration somewhere
  #__log.critical(message)
  pass

def get_potential_games(game):
    futures = []
    presenter = GamePresenter(game)
    for x, y in Moves(game).get_empty_positions():
        log("---- generating futures -----")
        log(presenter.dump_board_state())
        log("active player %s"%presenter.active_symbol())
        future = GameAIPresenter(game.clone())
        future.move(x,y,future.active_symbol())
        log("future board state is:")
        log(presenter.dump_board_state())
        log("future active player is: %s" % presenter.active_symbol())
        futures.append(((x,y),future))
    return futures

class GameAIPresenter(GamePresenter):

    def potential_next_states(self):
      return get_potential_games(self.game)
