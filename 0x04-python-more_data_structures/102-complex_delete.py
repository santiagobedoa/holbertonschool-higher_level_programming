#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())
    if value in values:
        while value in values:
            del a_dictionary[keys[values.index(value)]]
            values.pop(values.index(value))
    return a_dictionary
