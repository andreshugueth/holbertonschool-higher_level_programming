#!/usr/bin/python3
"""add_integer"""


def add_integer(a, b=98):
    """Represent addition

    Arguments:
        a {[int]} -- [First argument]

    Keyword Arguments:
        b {int} -- [Second argument] (default: {98})

    Raises:
        TypeError: [a must be an integer]
        TypeError: [b must be an integer]

    Returns:
        [int] -- [two numbers addition]
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
