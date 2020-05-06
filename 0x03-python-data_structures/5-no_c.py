#!/usr/bin/python3


def no_c(my_string):
    string = ''
    for pos in my_string:
        if pos == 'c' or pos == 'C':
            continue
        string = string + pos
    return string
