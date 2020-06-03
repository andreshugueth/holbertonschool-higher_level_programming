#!/usr/bin/python3
"""add atribute
"""


def add_attribute(obj, att, value):
    """add atribute function
    Arguments:
        obj {any} -- the object to add
        att {str} -- the name of the attribute to add
        value {any} -- the value of the attribute
    Raises:
        TypeError: can't add new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
