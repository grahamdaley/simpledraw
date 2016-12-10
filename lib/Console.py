"""
lib.Console
"""
from __future__ import print_function
import os
import sys

try:
    # Add commmand history support (up & down arrow keys), if available
    import readline
except ImportError:
    # Alas, readline module not available, so just forget it
    pass


# Make code Python 3.x.x compatible too
if sys.version[0] == "3":
    raw_input = input


class Console(object):
    """
    Manages the text console
    """

    ESC_POS = "\033[{0};{1}f"
    ESC_CLR_LINE = "\033[K"

    @staticmethod
    def clear_screen():
        """
        Clears the console
        """
        if os.name == 'nt':
            # for Windows
            os.system('cls')
        else:
            # for Linux / OSX
            os.system('clear')

    @staticmethod
    def print_at(row, column, text):
        """
        Displays the given text at the row & column position
        of the console

        Parameters
        ----------
        row : int
            Row to display the text at (1-based)
        column : int
            Column to display the text at (1-based)
        text : str
            The text string to display
        """
        print(Console.ESC_POS.format(str(row), str(column)) + text)

    @staticmethod
    def get_input(prompt=""):
        """
        Displays the given prompt text and accepts input
        from the keyboard

        Parameters
        ----------
        prompt : str
            The text string to prompt the user for input

        Returns
        -------
        str
            Text input by user, without any newline character
        """
        return raw_input(Console.ESC_POS.format(1, 1) + Console.ESC_CLR_LINE + prompt)
