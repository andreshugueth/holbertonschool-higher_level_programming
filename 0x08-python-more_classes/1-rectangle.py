#!/usr/bin/python3
"""Represent a rectangle"""


class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """initialization of rectangle class

        Keyword Arguments:
            width {int} -- width of the rectangle (default: {0})
            height {int} -- height of the rectangle (default: {0})
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """width property

        Returns:
            [int] -- width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Arguments:
            value {int} -- represent the width of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property

        Returns:
            [int] -- height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Arguments:
            value {int} -- height of the rectangle

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
