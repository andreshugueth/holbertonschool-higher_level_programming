#!/usr/bin/python3
"""Represent exact type of an object
"""


def is_same_class(obj, a_class):
    """Represent exact type of an object

    Arguments:
        obj {any} -- instance
        a_class {any} -- class

    Returns:
        [Bool] -- True or False
    """
    return (type(obj) == a_class)
