#!/usr/bin/python3
"""MyList class inherits from list
"""


class MyList(list):
    """Print a sorted list

    Arguments:
        list {list} -- Base class
    """
    def print_sorted(self):
        print(sorted(self))
