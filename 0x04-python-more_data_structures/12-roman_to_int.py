#!/usr/bin/python3


def roman_to_int(roman_string):
    hash_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    result = 0
    for i in range(0, len(roman_string)):
        if i + 1 < len(roman_string) and hash_map[roman_string[i]] < hash_map[roman_string[i + 1]]:
            result -= hash_map[roman_string[i]]
        else:
            result += hash_map[roman_string[i]]
    return result
