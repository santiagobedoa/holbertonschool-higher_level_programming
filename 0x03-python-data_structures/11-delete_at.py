#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        new_list = []
        for i, j in enumerate(my_list):
            if i != idx:
                new_list.append(j)
        my_list = new_list
        return new_list
