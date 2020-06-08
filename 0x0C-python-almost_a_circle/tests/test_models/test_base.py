#!/usr/bin/python3
"""Base Test"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base test class

    Args:
        unittest
    """
    def test_doc(self):
        """Docstring test"""
        self.assertTrue(len(Base.__doc__) > 1)

    def test_empty(self):
        """Empty id test"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

    def test_non_empty(self):
        """Non empty id test"""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base(15).id, 15)
