#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if (ord('a') <= ord(char) and ord(char) <= ord('z')):
            upper_char = chr(ord(char) - 32)
            print(upper_char, end="")
        else:
            print(char, end="")
    print("\n")
