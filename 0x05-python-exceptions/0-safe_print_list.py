#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    len_list = 0
    for element in my_list:
        print(element, end="")
        len_list += 1
        if len_list == x:
            break
    print("\n")
    return len_list
