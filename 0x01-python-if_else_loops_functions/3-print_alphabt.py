#!/usr/bin/python3
letter = ord('a')
while letter <= ord('z'):
    if (letter == ord('e') or letter == ord('q')):
        letter += 1
    else:
        print(chr(letter), end="")
        letter += 1
