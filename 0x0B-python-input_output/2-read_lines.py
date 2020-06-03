#!/usr/bin/python3
"""reads n number of lines
"""


def read_lines(filename="", nb_lines=0):
    """reads n number of lines of a text

    Keyword Arguments:
        filename {str} -- name of a file (default: {""})
        nb_lines {int} -- number of lines (default: {0})
    """
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for num, line in enumerate(f):
                if num in range(nb_lines):
                    print(line, end="")
