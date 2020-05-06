#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    condition = []
    for n in new_list:
        log = True if n % 2 == 0 else False
        condition.append(log)
    return condition
