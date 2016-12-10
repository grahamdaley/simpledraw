"""
lib.Canvas
"""
from __future__ import division
import os

class Canvas(object):
    """
    Canvas class - a simple memory-mapped drawing canvas
    """
    def __init__(self, width, height):
        """
        Parameters
        ----------
        width : int
            Required canvas width, in characters
        height : int
            Required canvas height, in lines
        """
        self.width = width
        self.height = height
        self._reset_frame_buffer()

    def _reset_frame_buffer(self):
        self.frame_buffer = [[' ' for _ in range(self.width + 2)] for _ in range(self.height + 2)]
        self.frame_buffer[0] = ['-' for _ in range(self.width + 2)]
        self.frame_buffer[-1] = ['-' for _ in range(self.width + 2)]
        for y in range(1, self.height + 1):
            self.frame_buffer[y][0] = '|'
            self.frame_buffer[y][-1] = '|'

    def _limit_coords(self, x, y):
        x = max(min(self.width, x), 1)
        y = max(min(self.height, y), 1)
        return (x, y)

    def _plot(self, coordinates, char):
        x, y = coordinates
        self.frame_buffer[y][x] = char

    def get_frame_buffer(self):
        """
        Returns the current contents of the canvas

        Returns
        -------
        str
            frame buffer as a multi-line string
        """
        return os.linesep.join(["".join([col for col in row]) for row in self.frame_buffer])

    def draw_line(self, x1, y1, x2, y2):
        """
        Draws a straight line from point (x1, y1) to (x2, y2) using Bresenham's
        Line Algorithm
        Gratuitously copied from RogueBasin:
        http://www.roguebasin.com/index.php?title=Bresenham%27s_Line_Algorithm#Python

        Parameters
        ----------
        x1 : int
            x-coordinate of the point at the start of the line
        y1 : int
            y-coordinate of the point at the start of the line
        x2 : int
            x-coordinate of the point at the end of the line
        y2 : int
            y-coordinate of the point at the end of the line
        """
        x1, y1 = self._limit_coords(x1, y1)
        x2, y2 = self._limit_coords(x2, y2)

        dx = x2 - x1
        dy = y2 - y1

        # Determine how steep the line is
        is_steep = abs(dy) > abs(dx)

        # Rotate line if necessary
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        # Swap start and end points if necessary and store swap state
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        # Recalculate differentials
        dx = x2 - x1
        dy = y2 - y1

        # Calculate error
        error = int(dx / 2.0)
        ystep = 1 if y1 < y2 else -1

        # Iterate over bounding box generating points between start and end
        y = y1
        for x in range(x1, x2 + 1):
            coord = (y, x) if is_steep else (x, y)
            self._plot(coord, 'x')
            error -= abs(dy)
            if error < 0:
                y += ystep
                error += dx

    def draw_rectangle(self, x1, y1, x2, y2):
        """
        Draws a rectange with the two diagonally-opposite corners
        given as (x1, y1) and (x2, y2)

        Parameters
        ----------
        x1 : int
            x-coordinate of the first corner of the rectange
        y1 : int
            y-coordinate of the first corner of the rectange
        x2 : int
            x-coordinate of the second corner of the rectange
        y2 : int
            y-coordinate of the second corner of the rectange
        """
        self.draw_line(x1, y1, x2, y1)
        self.draw_line(x2, y1, x2, y2)
        self.draw_line(x2, y2, x1, y2)
        self.draw_line(x1, y1, x1, y2)

    def fill(self, x, y, c):
        """
        Fill the area containing (x, y) with 'color' c
        using Flood Fill algorithm:
        https://en.wikipedia.org/wiki/Flood_fill

        Parameters
        ----------
        x1 : int
            x-coordinate of the target point
        y1 : int
            y-coordinate of the target point
        c : str
            the 'color' character
        """
        c = c[:1]
        x, y = self._limit_coords(x, y)

        if self.frame_buffer[y][x] != "x" and self.frame_buffer[y][x] != c:
            self.frame_buffer[y][x] = c

            # Recursively invoke fill on all surrounding cells:
            if x > 1:
                self.fill(x - 1, y, c)

            if x < self.width:
                self.fill(x + 1, y, c)

            if y > 1:
                self.fill(x, y - 1, c)

            if y < self.height:
                self.fill(x, y + 1, c)
