#!/usr/bin/python3
"""Peak exercise"""


def find_peak(list_of_integers):
    """find a peak in a list of int"""
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        m = find_peak(list_of_integers[1:])
        return m if m > list_of_integers[0] else list_of_integers[0]
