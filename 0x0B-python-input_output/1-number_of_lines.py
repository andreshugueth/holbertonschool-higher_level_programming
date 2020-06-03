#!/usr/bin/python3
"""function that count lines
"""


def number_of_lines(filename=""):
    """Count number of lines in a file

    Keyword Arguments:
        filename {str} -- name of a file (default: {""})

    Returns:
        [int] -- number of lines in a file
    """
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            count += 1
        return count
