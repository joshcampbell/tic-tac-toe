import logging

from ..game_ai_presenter import GameAIPresenter

WIN_SCORE = 100
DRAW_SCORE = 0
LOSS_SCORE = -100
OUT_OF_DEPTH_SCORE = 0

DEFAULT_DEPTH=6
HYPOTHETICAL_MAX_DEPTH=20

__log = logging.getLogger('ai')
__log.addHandler(logging.FileHandler('./tmp/ai.log'))

def log(message):
  # FIXME toggle logging based on configuration somewhere
  #__log.critical(message)
  pass

# FIXME uncovered
def best_moves(actual_game,symbol):
  return [pos for pos,score in Minimax(GameAIPresenter(actual_game),symbol).get_best_moves()]

class Minimax:

  def __init__(self,game,symbol,depth=None):
    if depth == None:
      depth=DEFAULT_DEPTH
    self.game = game
    self.symbol = symbol
    self.depth = depth

  def potential_games(self):
      return self.game.potential_next_states()

  def get_min_or_max(self,positions_with_scores):
      if self.game.active_symbol() == self.symbol:
          log("My turn, getting maximum")
          maximum = float("-inf")
          for pos, score in positions_with_scores:
              if score > maximum:
                  maximum = score
          return maximum
      else:
          log("Enemy turn, getting minumum")
          minimum = float("inf")
          for pos, score in positions_with_scores:
              if score < minimum:
                  minimum = score
          return minimum


  def get_best_moves(self):
      log("\n--- getting best move ---")
      log("current player is %s"%self.game.active_symbol())
      log(self.game.dump_board_state())
      scores = self.__positions_with_scores()
      log("scores of potential games: %s" % scores)
      min_or_max = self.get_min_or_max(scores)
      has_best_score = []
      for pos,score in scores:
          if score == min_or_max:
            has_best_score.append((pos,score))
      log(self.game.dump_board_state())
      log("best moves are %s"%has_best_score)
      log("\n--- got best moves ---")
      return has_best_score

  def __positions_with_scores(self):
      log("\n--- getting positions with scores---")
      return [ (pos,self.__get_score(presenter)) \
               for pos,presenter in self.potential_games()] 

  def __get_score(self, presenter): 
      log( "\n--- scoring board ---")
      log( presenter.dump_board_state())
      log( "depth = %s" % self.depth)
      score = float("-inf")
      if self.depth <= 0:
          log("out of depth") # FIXME uncovered
          score = OUT_OF_DEPTH_SCORE # FIXME uncovered
      if presenter.is_draw(): 
          log("game over: draw")
          score = DRAW_SCORE
      if presenter.winner() != None:
          depth_weight = HYPOTHETICAL_MAX_DEPTH - self.depth
          if presenter.winner() == self.symbol:
              log("game over: i won (self=%s,winner=%s)"%(self.symbol,presenter.winner()))
              score = WIN_SCORE - depth_weight
          else:
              log("game over: i lost (self=%s,winner=%s)"%(self.symbol,presenter.winner()))
              score = LOSS_SCORE + depth_weight
      if score == float("-inf"):
          log("getting recursive score")
          score = self.__get_recursive_score(presenter)
          log("recursive score is: %s" % score)
      log( presenter.dump_board_state())
      log("score for this board is %s\n" % score)
      log("----- done scoring board -----")
      return score

  def __get_recursive_score(self,presenter):
      log("------- getting recursive score -------")
      negamax = Minimax(presenter,self.symbol, self.depth-1)
      best_moves = negamax.get_best_moves()
      log("best moves are %s"%best_moves)
      log(presenter.dump_board_state())
      log("but i am returning %s"%best_moves[0][1])
      log("------ got recursive score ------")
      return best_moves[0][1]
