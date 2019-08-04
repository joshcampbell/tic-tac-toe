import curses
import random

import strings

# establish color palette indices
title_colors = 1
border_colors = 2
player_one_colors = 3
player_two_colors = 4

class RenderState():

  def __init__(self,game):
    self.board_size = game.board_size()
    self.origin_x = 0
    self.origin_y = 0
    self.border_width = 1
    self.square_size = 9
    self.tile_size = self.square_size + self.border_width
    self.total_board_size = self.square_size * self.board_size + \
                            (self.border_width * self.board_size)

class NotEnoughRoomException(Exception):
  pass

def centered_x(screen, string):
  screen_width = width(screen)
  diff = screen_width - len(string)
  if diff < 0:
    raise NotEnoughRoomException("%s > %s"%(len(string),screen_width))
  return diff // 2

def centered_y(screen,string):
  screen_height = height(screen)
  diff = screen_height - len(string.split("\n"))
  if diff < 0:
    raise NotEnoughRoomException("%s > %s"%(len(string),screen_height))
  return diff // 2

def board_offset_x(renderer, screen):
  return (width(screen) - renderer.total_board_size) // 2

def board_offset_y(renderer, screen):
  return (height(screen) - renderer.total_board_size) // 2

def draw_game_board(game,renderer, screen):
  positions = range(1,renderer.total_board_size)
  for x in positions:
    for y in positions:
      if (x % renderer.tile_size is 0 or y % renderer.tile_size is 0):
        draw_border(renderer, screen,y,x)
      else:
        draw_tile(game,renderer, screen,y,x)

def draw_border(renderer, screen,y,x):
  """
  Draws a piece of border / cross hatch on the screen at the specified position.
  """
  screen.attron(curses.color_pair(border_colors))
  screen.addstr(y + board_offset_y(renderer,screen),x + \
                   board_offset_x(renderer,screen)," ")

def draw_tile(game,renderer,screen,y,x):
  x_index = x // renderer.tile_size
  y_index = y // renderer.tile_size
  player = game.player_at(x_index+1,y_index+1)
  if player is not None:
    ordinality = game.ordinality(player)
    if ordinality is 1:
      screen.attron(curses.color_pair(player_one_colors))
    else:
      screen.attron(curses.color_pair(player_two_colors))
    screen.addstr(y + board_offset_y(renderer,screen),\
                  x + board_offset_x(renderer,screen),\
                  player["symbol"])

def player_string(player):
  return "%s is \"%s\""%(player["name"],player["symbol"]) 

def draw_top_bar(game,screen):
  # write player names
  screen.attron(curses.color_pair(player_one_colors))
  screen.addstr(0,0,player_string(game.player_one()))
  player_two_name = player_string(game.player_two())
  player_two_name = player_two_name.encode('utf-8')
  player_two_index = width(screen) - len(player_two_name)
  screen.attron(curses.color_pair(player_two_colors))
  screen.addstr(0,player_two_index,player_two_name)
  # indicate active player
  active_symbol = game.active_symbol()
  active_player_message = " %s's Turn " % active_symbol
  screen.attron(curses.color_pair(title_colors))
  print_centered(screen,0,active_player_message,curses.A_REVERSE)

def draw_bottom_bar(screen):
  bottom = height(screen) - 1
  message = "take [b]ack move :: click to move :: [q]uit"
  print_centered(screen, bottom, message)

def width(screen):
  height, width = screen.getmaxyx()
  return width

def height(screen):
  height, width = screen.getmaxyx()
  return height

def print_centered(screen,y,message,mode=curses.A_NORMAL):
  screen.addstr(y,centered_x(screen,message),message,mode)

def render_board(game,renderer,screen):
  screen.clear()
  draw_top_bar(game,screen)
  draw_bottom_bar(screen)
  draw_game_board(game,renderer,screen)
  screen.refresh()

def show_title(screen):
  screen.clear()
  screen.attron(curses.color_pair(border_colors))
  # draw the 'press any key' message across the top of the screen
  for x in range(0,width(screen)):
    screen.addstr(0,x," ")
  message = "   Press Any Key To Continue   "
  screen.addstr(0,centered_x(screen,message),message, curses.A_BOLD)
  screen.attron(curses.color_pair(title_colors))
  # draw the title (a multiline string) in the center
  title = random.choice(strings.titles)
  first_line = title.split("\n")[1]
  current_line = centered_y(screen,title)
  for line in title.split("\n"):
    current_line += 1
    screen.addstr(current_line,centered_x(screen,first_line),line)
  # wait for user input
  any_key = screen.getch()

def configure(screen):
  title_foreground = random.choice([curses.COLOR_WHITE,curses.COLOR_CYAN,curses.COLOR_MAGENTA,curses.COLOR_YELLOW,curses.COLOR_GREEN,curses.COLOR_RED])
  curses.init_pair(title_colors, title_foreground, curses.COLOR_BLACK)
  curses.init_pair(border_colors, curses.COLOR_BLACK, curses.COLOR_WHITE)
  curses.init_pair(player_one_colors, curses.COLOR_BLACK, curses.COLOR_CYAN)
  curses.init_pair(player_two_colors, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
  curses.curs_set(0) # hide cursor
  curses.mousemask(1) # enable mouse support
  curses.noecho()

def verify(renderer,screen):
  assert curses.has_colors(), "This game requires a color terminal."
  window_size = screen.getmaxyx()
  while (window_size[0] < renderer.total_board_size) \
        and (window_size[1] < renderer.total_board_size):
    "Terminal must be at least %sx%s characters"%(total_board_size,total_board_size)
    os.sleep(1)
