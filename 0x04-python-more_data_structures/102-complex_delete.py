#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    for elem in list(a_dictionary.keys()):
        if a_dictionary[elem] == value:
            del a_dictionary[elem]
    return a_dictionary
