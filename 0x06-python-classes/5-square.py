#!/usr/bin/python3
"""square class"""


class Square:
    """Represent a square
    Arguments:
        size: size of a square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Represent the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """Represent square printed by #"""
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()

    @property
    def size(self):
        """Represent the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Represent size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
