#!/usr/bin/python3
"""Text identation"""


def text_indentation(text):
    """Represent text identation
    Arguments:
        text {str} -- paragraph
    Raises:
        TypeError: text must be a string
    """
    if (text):
        if type(text) is str:
            comp = ['.', '?', ':']
            new_text = ""
            for elem in text:
                new_text += elem
                if elem in comp:
                    print(new_text.strip())
                    print()
                    new_text = ""
            print(new_text.strip(), end="")
        else:
            raise TypeError("text must be a string")
