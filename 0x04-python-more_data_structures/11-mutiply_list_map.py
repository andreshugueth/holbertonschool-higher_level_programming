#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    new_list = my_list[:]
    result = map(lambda x: x * number, new_list)
    return list(result)
