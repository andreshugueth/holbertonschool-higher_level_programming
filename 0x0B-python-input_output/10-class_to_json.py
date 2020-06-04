#!/usr/bin/python3
"""Returns the dictionary description
with simple data structure
"""


def class_to_json(obj):
    """returns the dictionary description

    Arguments:
        obj {any} -- type of object

    Returns:
        [type] -- [description]
    """
    return (obj.__dict__)
