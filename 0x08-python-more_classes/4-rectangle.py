#!/usr/bin/python3
"""Defining a Rectangle class."""


class Rectangle:
    """Representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.

        Args:
            width: The width of the new rectangle.
            height: The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returning an area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returning a perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returning a printable representation of the Rectangle.

        Representing a rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_new = []
        for itr in range(self.__height):
            [rect_new.append('#') for j in range(self.__width)]
            if itr != self.__height - 1:
                rect_new.append("\n")
        return ("".join(rect_new))

    def __repr__(self):
        """Returning a string representation of the Rectangle."""
        rect_new = "Rectangle(" + str(self.__width)
        rect_new += ", " + str(self.__height) + ")"
        return (rect_new)
