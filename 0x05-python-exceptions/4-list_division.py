#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    idx = 0
    new_list = [0 for idx in range(list_length)]
    for elem in new_list:
        try:
            new_list[idx] = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        finally:
            idx += 1
    return (new_list)
