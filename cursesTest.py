#!/bin/env python

# basic curses application

import curses

def application(stdscr):
  # Set up stdScr
  stdscr.clear()
  curses.nocbreak()
  curses.echo()

  # add str
  stdscr.addstr(1,1, "Hello and welcome press enter to contiunue")

  stdscr.getch()

  (maxrow, maxcol) = stdscr.getmaxyx()

  outwin = curses.newwin(maxrow - 10, maxcol - 2, 1, 1)
  outwin.box()
  inwin = curses.newwin(8, maxcol - 2,maxrow - 8 , 1)
  inwin.box()

  stdscr.clear()

  outwin.refresh()
  outwin.immedok(True)
  inwin.immedok(True)

  inwin.addstr(1,1,'>')

  string = inwin.getstr(1,3)

  outwin.addstr(1,1, string)

  inwin.getch()

# Go
curses.wrapper(application)