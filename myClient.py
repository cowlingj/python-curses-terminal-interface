"""

IRC client exemplar.

"""

import sys
from ex3utils import Client

import time

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

  # outwin.addstr(1,1, string)

  class IRCClient(Client):

    def onMessage(self, socket, message):
    # *** process incoming messages here ***

    outwin.addstr(1,1, message)

    ## TO DO MAKE THE ABOVE SCROLL UPWARDS (RECURSION MAY HELP)

    return True


    # Parse the IP address and port you wish to connect to.
    ip = sys.argv[1]
    port = int(sys.argv[2])
    screenName = sys.argv[3]

    # Create an IRC client.
    client = IRCClient()

    # Start server
    client.start(ip, port)

    # register your client here
    client.send('USERNAME %s' % screenName)

    while client.isRunning():
      try:
        # TO DO USE CURSES TO MOVE THE RAW INPUT TO THE BOTTOM
        # ADD A LINE ABOVE INPUT
        # ADD A BOX ABOVE WHERE THE TEXT GOES

        inwin.addstr(1,1,'>')

        command = inwin.getstr(1,3).strip


        # command = raw_input("> ").strip()
        client.send(command)
        # *** process input from the user in a loop here ***
        # *** use client.send(someMessage) to send messages to the server
      except:
        client.stop();

    client.stop()

curses.wrapper(application)


