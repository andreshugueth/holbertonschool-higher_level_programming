#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """Represent a locked class
    Just let the user create the instance attribute 'first_name'
    """
    __slots__ = ['first_name']
