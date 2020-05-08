#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string)  != str or roman_string is None:
        return 0
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    conv = 0
    prev = 0
    for pos in roman_string:
        num = numbers[pos]
        if prev < num:
            aux = num - prev * 2
            prev = num
            conv += aux
            continue
        prev = num
        conv += num

    return conv
