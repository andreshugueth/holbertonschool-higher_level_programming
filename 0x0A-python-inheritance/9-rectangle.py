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

    def area(self):
        """area of a rectangle

        Returns:
            [int] -- area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """str

        Returns:
            [str] -- returns a message
        """
        str = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return str
