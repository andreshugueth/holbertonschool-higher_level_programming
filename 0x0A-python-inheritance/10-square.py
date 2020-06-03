#!/usr/bin/python3
"""Represent a square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square class"""
    def __init__(self, size):
        """Constructor

        Arguments:
            size {int} -- size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Represent the area of a square

        Returns:
            [int] -- area of a square
        """
        return self.__size ** 2
