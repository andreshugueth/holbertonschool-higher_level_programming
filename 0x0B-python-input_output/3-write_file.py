#!/usr/bin/python3
"""write a file
"""


def write_file(filename="", text=""):
    """create and write a text in a file

    Keyword Arguments:
        filename {str} -- name of the file (default: {""})
        text {str} -- content of the file (default: {""})

    Returns:
        [int] -- number of characters
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
