#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for index, item in enumerate(my_list):
            if index == x:
                break
            print("{}".format(item), end='')
            count += 1
        print()
        return count
    except:
        return count
