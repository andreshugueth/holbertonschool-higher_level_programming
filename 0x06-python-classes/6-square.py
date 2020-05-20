#!/usr/bin/python3
"""Square class"""


class Square:
    """define size
    Arguments:
        size: size of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[1]) is not int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

    def area(self):
        """area of square"""
        return self.__size ** 2

    def my_print(self):
        if self.size > 0:
            if self.position[1] > 0:
                for newline in range(self.position[1]):
                    print("")
            for row in range(self.size):
                if self.position[0] > 0:
                    for spaces in range(self.position[0]):
                        print(" ", end="")
                for collumn in range(self.size):
                    print("#", end="")
                print("")
        else:
            print("")

    @property
    def size(self):
        """getter function"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter size function"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """positional value"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
