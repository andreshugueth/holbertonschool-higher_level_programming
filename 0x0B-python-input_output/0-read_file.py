#!/usr/bin/python3
"""Function that reads
a text file
"""


def read_file(filename=""):
    """Reads a text file with UTF8 encode

    Keyword Arguments:
        filename {str} -- name of the file (default: {""})
    """
    with open(filename, encoding='utf-8') as f:
        f_contents = f.read()
        print(f_contents, end="")
