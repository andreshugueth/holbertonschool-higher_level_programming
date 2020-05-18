#!/usr/bin/python3


def safe_print_division(a, b):
    op = 0
    try:
        op = a / b
    except ZeroDivisionError:
        op = None
    finally:
        print('Inside result: {}'.format(op))
        return op
