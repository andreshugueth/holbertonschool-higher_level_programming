#!/usr/bin/python3
"""Unittest for base"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class

    Args:
        unittest
    """
    def test_doc(self):
        """doc test"""
        self.assertTrue(len(Base.__doc__) > 1)

    def test_not_empty(self):
        """not empty id"""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base(15).id, 15)

    def test_empty(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
