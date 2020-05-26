#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Represent a rectangle"""

    # count instances
    number_of_instances = 0
    # symbol
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialization of rectangle class
        Keyword Arguments:
            width {int} -- width of the rectangle (default: {0})
            height {int} -- height of the rectangle (default: {0})
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            value {int} -- width of the rectangle
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
            value {[int]} -- height of the rectangle
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle
        Returns:
            [int] -- area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """perimeter of the rectangle
        Returns:
            [int] -- perimeter of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * self.height + 2 * self.width

    def __str__(self):
        """str method
        Returns:
            [str] -- print rectangle in #
        """
        prt = ""
        if self.width == 0 or self.height == 0:
            return prt
        for elem in range(0, self.height):
            prt += ("{}".format(self.print_symbol)) * self.width
            if elem != self.height - 1:
                prt += '\n'
        return prt

    def __repr__(self):
        """repr method
        Returns:
            [str] -- rectangle properties
        """
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        """destructor method
        """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
