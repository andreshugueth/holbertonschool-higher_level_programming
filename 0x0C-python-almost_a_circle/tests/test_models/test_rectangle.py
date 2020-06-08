#!/usr/bin/python3
"""rectangle test"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_doc(self):
        """Docstring test"""
        self.assertTrue(len(Rectangle.__doc__) > 1)

    def test_non_empty(self):
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)
