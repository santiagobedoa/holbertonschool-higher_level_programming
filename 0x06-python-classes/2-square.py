#!/usr/bin/python3
"""defines a Square Class"""


class Square:
    """Represents a Square"""

    def __init__(self, size):
        """initializes"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
