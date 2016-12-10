"""
lib.TestCommand
"""
from lib.Command import Command
import unittest

class TestCommand(unittest.TestCase):
    """
    Tests the Command class methods
    """
    def test_valid1(self):
        parsed_command = Command.parse("C 20 4", 0, 0)
        self.assertEqual(parsed_command["verb"], "C", "incorrect command verb")
        self.assertEqual(parsed_command["width"], 20, "incorrect width")
        self.assertEqual(parsed_command["height"], 4, "incorrect height")

    def test_valid2(self):
        parsed_command = Command.parse("L 1 2 6 2", 20, 20)
        self.assertEqual(parsed_command["verb"], "L", "incorrect command verb")
        self.assertEqual(parsed_command["x1"], 1, "incorrect x1 value")
        self.assertEqual(parsed_command["y1"], 2, "incorrect y1 value")
        self.assertEqual(parsed_command["x2"], 6, "incorrect x2 value")
        self.assertEqual(parsed_command["y2"], 2, "incorrect y2 value")

    def test_valid3(self):
        parsed_command = Command.parse("R 16 1 20 3", 20, 20)
        self.assertEqual(parsed_command["verb"], "R", "incorrect command verb")
        self.assertEqual(parsed_command["x1"], 16, "incorrect x1 value")
        self.assertEqual(parsed_command["y1"], 1, "incorrect y1 value")
        self.assertEqual(parsed_command["x2"], 20, "incorrect x2 value")
        self.assertEqual(parsed_command["y2"], 3, "incorrect y2 value")

    def test_valid4(self):
        parsed_command = Command.parse("B 10 3 o", 20, 20)
        self.assertEqual(parsed_command["verb"], "B", "incorrect command verb")
        self.assertEqual(parsed_command["x1"], 10, "incorrect x1 value")
        self.assertEqual(parsed_command["y1"], 3, "incorrect y1 value")
        self.assertEqual(parsed_command["c"], "o", "incorrect c value")

    def test_valid5(self):
        parsed_command = Command.parse("Q", 20, 20)
        self.assertEqual(parsed_command["verb"], "Q", "incorrect command verb")

    def test_invalid1(self):
        parsed_command = Command.parse("S 1 2 3 4", 20, 20)
        self.assertEqual(parsed_command["verb"], Command.ERROR,
                         "failed to notice invalid command verb, 'S'")

    def test_invalid2(self):
        parsed_command = Command.parse("L 1 2 j 2", 20, 20)
        self.assertEqual(parsed_command["verb"], Command.ERROR,
                         "failed to notice invalid argument type, 'j' (should be int)")

    def test_invalid3(self):
        parsed_command = Command.parse("B 1 2 ooo", 20, 20)
        self.assertEqual(parsed_command["verb"], Command.ERROR,
                         "failed to notice invalid argument type, 'ooo' (should be single char)")
        self.assertEqual(parsed_command[Command.ERROR_REASON], Command.REASON_ARG_TYPE,
                         "failed to note reason for invalid argument (invalid type)")

    def test_invalid4(self):
        parsed_command = Command.parse("B 1 2", 20, 20)
        self.assertEqual(parsed_command["verb"], Command.ERROR,
                         "failed to notice missing argument, c")
        self.assertEqual(parsed_command[Command.ERROR_REASON], Command.REASON_ARG_MISSING,
                         "failed to note reason being a missing argument")

    def test_invalid5(self):
        parsed_command = Command.parse("L 1 2 6 2", 5, 5)
        self.assertEqual(parsed_command["verb"], Command.ERROR,
                         "failed to notice invalid argument, x2 (out of range)")
        self.assertEqual(parsed_command[Command.ERROR_REASON], Command.REASON_COORD_RANGE,
                         "failed to note reason for invalid argument, x2 (out of range)")
