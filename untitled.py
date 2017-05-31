#!/bin/env python

# basic curses application

import curses

def application():
  # Set up stdScr
  stdScr = curses.initScr()
  stdScr.clear()

  # add str
  stdScr.mvaddstr(10,10, "Hello")


curses.wrapper(application)