#!/usr/bin/python3
"""defines a Square Class"""


class Square:
    """Represents a Square"""

    def __init__(self, size):
        """initializes"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
