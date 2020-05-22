#!/usr/bin/python3
"""add_integer"""


def add_integer(a, b=98):
    """Represent add_integer
    Arguments:
    a: 
    b: 
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
