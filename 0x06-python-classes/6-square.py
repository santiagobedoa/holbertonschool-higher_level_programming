#!/usr/bin/python3
"""defines a Square Class"""


class Square:
    """Represents a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates the square's area"""
        return (self.__size) ** 2

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if all(pos.isdigit() for pos in self.__position) and\
           len(self.__position) == 2 and\
           type(value) in not tuple:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for j in range(self.__size):
            print(f"{self.__position[0] * ' '}{self.__size * '#'}")
