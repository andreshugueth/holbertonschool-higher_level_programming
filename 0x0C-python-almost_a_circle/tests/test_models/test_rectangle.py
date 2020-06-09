#!/usr/bin/python3
"""rectangle test"""
import unittest
from models.base import Base
from models import rectangle
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""
    def test_doc(self):
        """Docstring test"""
        self.assertTrue(len(Rectangle.__doc__) > 1)

    def test_non_empty(self):
        """non empty test"""
        self.assertEqual(Rectangle(10, 2).id, 2)
        self.assertEqual(Rectangle(2, 10, 3).id, 3)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_values(self):
        """raises test"""
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(TypeError, Rectangle, "10", 2)
        self.assertRaises(ValueError, Rectangle, -10, 2)
        self.assertRaises(ValueError, Rectangle, 10, -2)
        self.assertRaises(TypeError, Rectangle, 10, 2, {})
        self.assertRaises(ValueError, Rectangle, 10, 2, 3, -1)

    def test_area(self):
        """test area"""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
