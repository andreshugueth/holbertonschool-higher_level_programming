#!/usr/bin/python3
"""print square"""


def print_square(size):
    """Represent a square
    Arguments:
    size {int} size of the square size x size

    raise:

    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for n in range(size):
        print("#" * size)
