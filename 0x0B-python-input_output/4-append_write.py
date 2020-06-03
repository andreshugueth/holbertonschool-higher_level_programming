#!/usr/bin/python3
"""appends a text in a file
"""


def append_write(filename="", text=""):
    """appends a text in a file

    Keyword Arguments:
        filename {str} -- name of the file (default: {""})
        text {str} -- appended text (default: {""})

    Returns:
        [int] -- number of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
        return (len(text))
