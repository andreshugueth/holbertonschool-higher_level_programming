#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    oper = [[elem * elem for elem in row] for row in new_matrix]
    return oper
