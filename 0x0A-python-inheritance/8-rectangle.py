#!/usr/bin/python3
"""Rectangle subclass from Basegeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle"""
    def __init__(self, width, height):
        """Constructor

        Arguments:
            width {int} -- width of a rectangle
            height {int} -- height of a rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
