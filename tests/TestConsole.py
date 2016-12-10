"""
tests.TestConsole
"""
from __future__ import print_function
from lib.Console import Console
from contextlib import contextmanager
import os
import sys
import unittest

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO


@contextmanager
def stdout_redirected(to=os.devnull, stdout=None):
    """
    Redirects stdout to file 'to', so tests can validate the console output
    """
    if stdout is None:
        stdout = sys.stdout

    # Copy stdout_fd before it is overwritten
    stdout_fd = stdout.fileno()

    with os.fdopen(os.dup(stdout_fd), 'wb') as copied:
        # Flush library buffers that dup2 knows nothing about
        stdout.flush()
        with open(to, 'wb') as to_file:
            os.dup2(to_file.fileno(), stdout_fd)
        try:
            # Allow code to be run with the redirected stdout
            yield stdout
        finally:
            # Restore stdout to its previous value
            stdout.flush()
            os.dup2(copied.fileno(), stdout_fd)


class TestConsole(unittest.TestCase):
    """
    Tests the Console class methods
    """
    def setUp(self):
        self.stdout_filename = "test.out"

    def tearDown(self):
        if os.path.exists(self.stdout_filename):
            os.remove(self.stdout_filename)

    def _read_output(self):
        with open(self.stdout_filename, 'r') as output_file:
            lines = output_file.readlines()

        return lines

    def test_valid_print_at(self):
        test_string = "Hello, world"

        with stdout_redirected(to=self.stdout_filename):
            Console.print_at(2, 2, test_string)

        output = self._read_output()[0]
        expected = Console.ESC_POS.format(2, 2) + test_string

        self.assertEqual(output.rstrip(), expected, "print_at failed, incorrect console output")

    def test_valid_console_input(self):
        test_input = "Hello, world"
        test_prompt = "Type something:"

        with stdout_redirected(to=self.stdout_filename):
            try:
                sys.stdin = StringIO(test_input)
                console_input = Console.get_input(test_prompt)
            finally:
                sys.stdin = sys.__stdin__

        output = self._read_output()[0]
        expected_output = Console.ESC_POS.format(1, 1) + Console.ESC_CLR_LINE + test_prompt

        self.assertEqual(output, expected_output, "get_input failed, incorrect input prompt")
        self.assertEqual(console_input, test_input, "get_input failed, incorrect console input")
