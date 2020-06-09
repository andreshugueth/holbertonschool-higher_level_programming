#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x dimension getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x dimension setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y dimension getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y dimension setter"""
        if type(y) != int:
            raise TypeError("y mus be an integer")
        elif (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """rectangle area"""
        return self.__width * self.__height

    def display(self):
        """Display rectangle"""
        for elem in range(self.__height):
            print("#" * self.__width)
