#!/usr/bin/python3
"""Function that insert a line to a file"""


def append_after(filename="", search_string="", new_string=""):
    """appends after a line

    Keyword Arguments:
        filename {str} -- name of the file (default: {""})
        search_string {str} -- searched string (default: {""})
        new_string {str} -- new string (default: {""})
    """
    text = ""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w') as f:
        f.write(text)
