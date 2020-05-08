#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list:
        divident = 0
        divisor = 0
        for n1, n2 in my_list:
            divident += n1 * n2
            divisor += n2
        return divident / divisor
