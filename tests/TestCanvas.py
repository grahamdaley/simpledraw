"""
tests.TestCanvas
"""
from lib.Canvas import Canvas
import unittest

class TestCanvas(unittest.TestCase):
    """
    Tests the Canvas class methods
    """
    def setUp(self):
        self.canvas = Canvas(20, 4)

    def test_canvas_size(self):
        canvas = Canvas(30, 40)
        self.assertEqual(canvas.width, 30, "incorrect canvas width")
        self.assertEqual(canvas.height, 40, "incorrect canvas height")

    def test_line1(self):
        self.canvas.draw_line(1, 2, 6, 2)
        expected_buf = """----------------------
|                    |
|xxxxxx              |
|                    |
|                    |
----------------------"""
        self.assertEqual(self.canvas.get_frame_buffer(), expected_buf,
                         "draw_line failed to draw horizontal line correctly")

    def test_line2(self):
        self.canvas.draw_line(6, 3, 6, 4)
        expected_buf = """----------------------
|                    |
|                    |
|     x              |
|     x              |
----------------------"""
        self.assertEqual(self.canvas.get_frame_buffer(), expected_buf,
                         "draw_line failed to draw vertical line correctly")

    def test_line3(self):
        self.canvas.draw_line(1, 1, 4, 4)
        expected_buf = """----------------------
|x                   |
| x                  |
|  x                 |
|   x                |
----------------------"""
        self.assertEqual(self.canvas.get_frame_buffer(), expected_buf,
                         "draw_line failed to draw diagonal line correctly")

    def test_rect(self):
        self.canvas.draw_rectangle(16, 1, 20, 3)
        expected_buf = """----------------------
|               xxxxx|
|               x   x|
|               xxxxx|
|                    |
----------------------"""
        self.assertEqual(self.canvas.get_frame_buffer(), expected_buf,
                         "draw_line failed to draw diagonal line correctly")

    def test_fill1(self):
        self.canvas.draw_rectangle(16, 1, 20, 3)
        self.canvas.fill(17, 2, 'o')
        expected_buf = """----------------------
|               xxxxx|
|               xooox|
|               xxxxx|
|                    |
----------------------"""
        self.assertEqual(self.canvas.get_frame_buffer(), expected_buf,
                         "fill failed")

    def test_fill2(self):
        self.canvas.draw_rectangle(16, 1, 20, 3)
        self.canvas.draw_line(3, 1, 3, 4)
        self.canvas.fill(4, 2, '#')
        expected_buf = """----------------------
|  x############xxxxx|
|  x############x   x|
|  x############xxxxx|
|  x#################|
----------------------"""
        self.assertEqual(self.canvas.get_frame_buffer(), expected_buf,
                         "fill failed")
