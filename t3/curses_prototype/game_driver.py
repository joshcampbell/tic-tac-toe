from __future__ import division

# NOTE I wrote this around the curses API, without building any kind of
#      abstraction layer. That means it's entirely procedural. It also wasn't
#      test-driven, since I didn't want to go down a rabbit hole about how to
#      test curses applications. That may have been a bad decision.
#
#      At this point, as far as forward development is concerned, I would comb
#      over this prototype to generate a set of functional requirements, then
#      discard it and restart the implementation from scratch.

import curses
import random
import locale
import logging
import json

from sys import exit
from locale import setlocale

from ..game import Game
from ..game_presenter import GamePresenter
from ..ai.minimax import best_moves
from ..exceptions import ImpossibleMoveException, NoMovesToUndoException

from voice import Voice

import screen
from screen import RenderState
import strings

import os

setlocale(locale.LC_ALL, '')

config = json.loads(str(open("./settings.json").read()))
game = GamePresenter(Game(config))
renderer = render_state = RenderState(game)
voice = Voice()

def main(curses_screen):
  #FIXME extract object from screen module
  screen.verify(renderer, curses_screen)
  screen.configure(curses_screen)
  voice.say(random.choice(strings.TITLE_SCREEN_MESSAGES)%
                  (game.player_one()["name"], game.player_one()["symbol"],
                   game.player_two()["name"], game.player_two()["symbol"]))
  screen.show_title(curses_screen)
  game_loop(curses_screen)
  voice.say("Goodbye")

QUIT_KEYS = [ ord('q'),
              # 27 is esc
              27 ]

BACK_KEYS = [ ord('b') ]


def game_loop(curses_screen):
  voice.say(" ".join([random.choice(strings.START_OF_PLAY_MESSAGES),
                      random.choice(strings.INDICATE_CLICKING_MESSAGES)]))
  while True:
    screen.render_board(game,renderer,curses_screen)
    key_pressed = curses_screen.getch()
    if key_pressed in QUIT_KEYS:
      break
    if key_pressed in BACK_KEYS:
      take_back_move(game)
    if key_pressed == curses.KEY_MOUSE:
      if not game.is_over():
        _, x, y, __, click_type = curses.getmouse()
        try:
          perform_player_move(renderer,curses_screen,x,y)
          screen.render_board(game,renderer,curses_screen)
          perform_ai_move(game,renderer,x,y)
        except ImpossibleMoveException as e:
          voice.say(random.choice(strings.CANNOT_MOVE_MESSAGES))

def take_back_move(game):
      try:
        game.moves.undo()
        voice.say("Undone")
      except NoMovesToUndoException:
        voice.say("No")

def perform_player_move(renderer,curses_screen,x,y):
        x -= screen.board_offset_x(renderer, curses_screen)
        y -= screen.board_offset_y(renderer, curses_screen)
        advance_game(\
          x_pos = (x // renderer.tile_size) + 1, \
          y_pos = (y // renderer.tile_size) + 1 \
        )

def perform_ai_move(game,renderer,x,y):
          voice.say(random.choice(strings.THINKING_MESSAGES))
          moves = best_moves(game.game,game.player_two_symbol())
          if len(moves) > 0:
            x, y = list(random.choice(moves))
            advance_game(x,y)
          else:
            voice.say("I cannot move.")
            game.change_player()

def advance_game(x_pos,y_pos):
  game.move(x_pos,y_pos, game.active_symbol())
  voice.say("DONE. %s TO %s %s"%(game.player_two()["symbol"],x_pos,y_pos))
  winner = game.winner()
  if game.is_draw():
    show_draw_message()
  if winner == game.player_one_symbol():
    voice.say(strings.LOSS_MESSAGE)
  if winner == game.player_two_symbol():
    voice.say(random.choice(strings.VICTORY_MESSAGES));

def show_draw_message():
  voice.say("Game Ends in Draw")

def show_winner(winner):
  voice.say("%s Wins"%winner)
