#!/usr/bin/python3
"""Defining a Rectangle class."""


class Rectangle:
    """Representing a rectangle.

    Attributes:
        number_of_instances: The number of Rectangle instances.
        print_symbol: The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.

        Args:
            width: The width of the new rectangle.
            height: The height of the new rectangle.
        """
        type(self).number_of_instances += 1
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
        """Returning a area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returning a perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returning a Rectangle with the greater area.

        Args:
            rect_1: The first Rectangle.
            rect_2: The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Returning a printable representation of the Rectangle.

        Representing a rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for itr in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if itr != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returning a string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Printing the message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
