#!/usr/bin/python3
"""print square"""


def print_square(size):
    """Represent square printing

    Arguments:
        size {[int]} -- [size of the square]

    Raises:
        TypeError: [size must be an integer]
        ValueError: [size must be >= 0]
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for n in range(size):
        print("#" * size)
