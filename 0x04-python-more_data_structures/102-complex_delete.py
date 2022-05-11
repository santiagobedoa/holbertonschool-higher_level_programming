#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    # keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())
    if value in values:
        # del a_dictionary[keys[values.index(value)]]
        return {x: y for x, y in a_dictionary.items() if y != value}
    return a_dictionary
