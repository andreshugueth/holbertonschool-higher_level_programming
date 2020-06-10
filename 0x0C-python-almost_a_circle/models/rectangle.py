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

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x dimension getter"""
        return self.__x

    @property
    def y(self):
        """y dimension getter"""
        return self.__y

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """x dimension setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """y dimension setter"""
        if type(y) != int:
            raise TypeError("y mus be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """rectangle area"""
        return self.__width * self.__height

    def display(self):
        """Display rectangle"""
        for ypos in range(self.__y):
            print()
        for elem in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """str representation class"""
        msg = ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
               self.__x, self.__y, self.__width, self.__height))
        return msg

    def update(self, *args, **kwargs):
        """update function"""
        if len(args):
            for element, value in enumerate(args):
                if element == 0:
                    self.id = value
                if element == 1:
                    self.width = value
                if element == 2:
                    self.height = value
                if element == 3:
                    self.x = value
                if element == 4:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of Rectangle"""
        new_dict = {}
        new_dict["x"] = self.x
        new_dict["y"] = self.y
        new_dict["id"] = self.id
        new_dict["height"] = self.height
        new_dict["width"] = self.width
        return new_dict
