#!/usr/bin/python3
"""square class"""


class Square:
    """Represent a square
    Arguments:
        size: size of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Represent the area"""
        return self.__size ** 2

    def my_print(self):
        """Represent printing"""
        if self.__size < 0:
            print()
        else:
            if self.__position[1] > 0:
                for newline in range(self.__position[1]):
                    print("")
            for row in range(self.__size):
                if self.__position[0] > 0:
                    for spaces in range(self.__position[0]):
                        print(" ", end="")
                for collumn in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """Represent the size"""
        return self.__size

    @size.getter
    def size(self, value):
        """Represent size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Represent position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Represent pos setter"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
