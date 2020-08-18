#!/usr/bin/python3
"""Peak exercise"""


def find_peak(list_of_integers):
    """find a peak in a list of int"""
    if not list_of_integers:
        return None

    peak = list_of_integers[0]
    for i, elem in enumerate(list_of_integers):
        if i == 0:
            continue
        if list_of_integers[i - 1] < elem and list_of_integers[i + 1] < elem:
            peak = elem

    return peak
