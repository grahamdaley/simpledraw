#!/usr/bin/env python
"""
simpledraw - the world's simplest drawing program

Author     - Graham Daley
             graham@daleybread.com
"""
from __future__ import print_function
from lib.Canvas import Canvas
from lib.Command import Command
from lib.Console import Console
import os


DEFAULT_WIDTH = 40
DEFAULT_HEIGHT = 20
TOP = 1
LEFT = 1


def main_loop():
    """
    Main execution loop
    """
    canvas = Canvas(DEFAULT_WIDTH, DEFAULT_HEIGHT)
    Console.clear_screen()

    while True:

        Console.print_at(TOP + 1, LEFT, canvas.get_frame_buffer())

        command_line = Console.get_input("enter command: ")
        params = Command.parse(command_line, x_max=canvas.width, y_max=canvas.height)

        _hide_help(row=canvas.height + 3)

        if params['verb'] == 'C':
            Console.clear_screen()
            canvas = Canvas(params['width'], params['height'])
        elif params['verb'] == 'L':
            canvas.draw_line(params['x1'], params['y1'], params['x2'], params['y2'])
        elif params['verb'] == 'R':
            canvas.draw_rectangle(params['x1'], params['y1'], params['x2'], params['y2'])
        elif params['verb'] == 'B':
            canvas.fill(params['x1'], params['y1'], params['c'])
        elif params['verb'] == 'Q':
            Console.clear_screen()
            break
        else:
            if Command.ERROR_REASON in params and params[
                    Command.ERROR_REASON] == Command.REASON_COORD_RANGE:
                _show_help_coords(row=canvas.height + 4, max_x=canvas.width, max_y=canvas.height)
            else:
                _show_help_commands(row=canvas.height + 4)


def _show_help_coords(row, max_x, max_y):
    Console.print_at(row, LEFT, "Coordinates must be in the range (1, 1) to ({0}, {1})".format(
        max_x, max_y))


def _show_help_commands(row):
    Console.print_at(row, LEFT, """Invalid command. Please enter one of the following:

Command         Description
C w h           Creates a new canvas of width w and height h.
L x1 y1 x2 y2   Draws a line from (x1, y1) to (x2, y2).
R x1 y1 x2 y2   Draws a rectangle, whose upper left corner is (x1, y1) and
                lower right corner is (x2, y2).
B x y c         Fills the entire area connected to (x, y) with "colour" c.
Q               Quits the program.
                    """)


def _hide_help(row):
    Console.print_at(row, LEFT, (" " * 74 + os.linesep) * 10)


if __name__ == "__main__":
    main_loop()
