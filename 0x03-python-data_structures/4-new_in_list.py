#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    if idx < 0:
        return list_copy
    count = 0
    for n in list_copy:
        count += 1
    if idx < count:
        list_copy[idx] = element
        return list_copy
    else:
        return list_copy
