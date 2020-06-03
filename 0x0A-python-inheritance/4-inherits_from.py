#!/usr/bin/python3
"""Represent inherited directly
or indirectly from an specified class
"""


def inherits_from(obj, a_class):
    """Represent inherited directly
    or indirectly from an specified class

    Arguments:
        obj {any} -- inherited obj
        a_class {any} -- class

    Returns:
        [Bool] -- True or False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
