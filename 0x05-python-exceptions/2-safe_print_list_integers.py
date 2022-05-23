#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(0, x):
        try:
            print("{:d}".format())
            counter += 1
        except (IndexError, TypeError, ValueError):
            pass
    print("")
    return (counter)
