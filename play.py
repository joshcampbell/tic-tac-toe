#!/usr/bin/env python
import curses

from t3.curses_prototype.game_driver import main

curses.wrapper(main)
print "Thanks for playing!"
