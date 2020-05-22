#!/usr/bin/python3
"""Say my name class"""


def say_my_name(first_name, last_name=""):
    """Represent name

    Arguments:
        first_name {str} -- First name
    
    keyword Arguments:
        last_name  {str} -- Last name (default: {""})

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
