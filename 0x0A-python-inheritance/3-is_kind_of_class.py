#!/usr/bin/python3
"""Represent instance of a class or inherited from
"""


def is_kind_of_class(obj, a_class):
    """Represent instance of a class or inherited from

    Arguments:
        obj {any} -- instance or inherited
        a_class {any} -- class

    Returns:
        [Bool] -- True or False
    """
    return (isinstance(obj, a_class))
