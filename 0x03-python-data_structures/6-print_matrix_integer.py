#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in range(len(row)):
            if elem + 1 != len(row):
                print('{:d}'.format(row[elem]), end=' ')
            else:
                print('{:d}'.format(row[elem]), end='')
        print()
