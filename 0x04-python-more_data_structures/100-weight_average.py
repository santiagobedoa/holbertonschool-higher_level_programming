#!/usr/bin/python3


def weight_average(my_list=[]):
    divisor = sum([x[1] for x in my_list])
    result = 0
    for i in my_list:
        result += i[0] * i[1]
    return result / divisor
