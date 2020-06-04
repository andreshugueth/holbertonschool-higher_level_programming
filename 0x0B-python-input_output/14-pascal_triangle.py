#!/usr/bin/python3
"""Represent pascal_triangle
"""


def pascal_triangle(n):
    """Represent the function of a pascal triangle
    """
    if n <= 0:
        return ([])
    row = [1]
    y = [0]
    result = []
    for m in range(n):
        result.append(row)
        row = [x+r for x, r in zip(row+y, y+row)]
    return result
