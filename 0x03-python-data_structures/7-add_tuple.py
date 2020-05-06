#!/usr/bin/python3


def check_con(tuple_c, idx):
    if idx >= len(tuple_c):
        return 0

    return tuple_c[idx]


def add_tuple(tuple_a=(), tuple_b=()):
    a = check_con(tuple_a, 0) + check_con(tuple_b, 0)
    b = check_con(tuple_a, 1) + check_con(tuple_b, 1)

    return (a, b)
