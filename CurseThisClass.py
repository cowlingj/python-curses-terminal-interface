#!/bin/env python

import curses

"""
Curses
"""
class App:

  def __init__(self, welcomestring = None):
    (self.inwin, self.outwin) = curses.wrapper(self.__application, welcomestring)
    self.outwinline = 1
    (self.outwinmaxrow, self.outwinmaxcol) = self.outwin.getmaxyx()
    self.outwinmaxrow = self.outwinmaxrow - 1

  def __exit__(self):
    curses.nocbreak()
    self.window.keypad(0)
    self.outwin.keypad(0)
    self.stdscr.keypad(0)
    curses.echo()
    curses.endwin()


  def __application(self, stdscr, welcomestring = None):
    # Set up stdScr
    stdscr.clear()
    curses.nocbreak()
    curses.echo()

    # add welcome message
    if welcomestring != None:
      stdscr.addstr(1,1, welcomestring)
      stdscr.getch()

    # get the size of the terminal at the moment
    (maxrow, maxcol) = stdscr.getmaxyx()

    # create two windows, one for input, one for output, give them borders
    outwin = curses.newwin(maxrow - 4, maxcol, 0, 0)
    outwin.box()
    inwin = curses.newwin(4, maxcol, maxrow - 4, 0)
    inwin.box()

    # clear the screen of the welcome message
    stdscr.clear()

    # refresh the screens and set to auto-frefresh
    outwin.refresh()
    outwin.immedok(True)
    inwin.immedok(True)

    inwin.addstr(1,2,'>')

    return (inwin, outwin)

  # Gets the message typed into the prompt (inwin)
  def getMessage(self):
    message = self.inwin.getstr(1,4)
    self.inwin.clear()
    self.inwin.box()
    self.inwin.addstr(1, 2, '>')
    return message

  # takes a message and displays it (on the outwin)
  def setResponse(self, message):
    # if the message is too big to fit on screen break it down
    maxlength = self.outwinmaxcol - 4
    if len(message) > maxlength:
      parts = []
      for length in range (0, len(message), maxlength):
        parts.append(message[length:length + maxlength])
      for part in parts:
        self.setResponse(part)
    else:
      # if the message would be placed outside the border, scroll all lines up
      if self.outwinline == self.outwinmaxrow:
        self.__scroll(self.outwinmaxrow - 1 , message)
      else:
        self.outwin.addstr(self.outwinline, 2, message)
        self.outwinline = self.outwinline + 1

  # recursively copy the text from each row starting with the bottom,
  # clear the screen and (with the exception of the top line) paste that text
  # into the line above
  def __scroll(self, row, message):
    if row == 1:
      self.outwin.refresh()
    else:
      currentline = self.outwin.instr(row, 1, self.outwinmaxcol - 1)
      self.__scroll(row - 1, message)
      self.outwin.addstr(row - 1, 1, currentline)
    if message == "":
      self.outwin.addstr(row, 2, " ")
    else:
      self.outwin.addstr(row, 2, message)
    self.outwin.box()
"""
class win:
  def __enter__(self, window):
    self.window = window
    return self

  def __exit__(self, type, value, traceback):
    curses.nocbreak();
    self.window.keypad(0);
    curses.echo()
"""



if __name__ == "__main__":
  app = App("""Hello and welcome, press enter to continue""")

  while True:
    message = app.getMessage()
    app.setResponse(message)
    