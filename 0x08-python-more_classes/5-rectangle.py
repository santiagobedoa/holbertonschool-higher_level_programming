#!/usr/bin/python3
""" Module for Rectangle class. """


class Rectangle:
    """
    Representation of a Rectangle.
    """

    def __init__(self, width=0, height=0):
        """ initialization """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    def area(self):
        """ Returns the area of the Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the area of the Rectangle """
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ Returns string representation with '#' """
        if not self.__width or not self.__height:
            return " "
        return (("#" * self.__width + '\n') * self.height)[:-1]

    def __repr__(self):
        """ Returns formal string representation """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"

    def __del__(self):
        """ Destructor """
        print("Bye rectangle...")
