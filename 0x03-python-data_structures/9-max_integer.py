#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) > 0:
        max_value = 0
        for i in my_list:
            if i > max_value:
                max_value = i
        return max_value
    return None
