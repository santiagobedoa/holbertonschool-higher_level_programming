#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        higher_score = max(list(a_dictionary.values()))
        return (list(a_dictionary.keys())[list(a_dictionary.values()).index(higher_score)])
    return None
