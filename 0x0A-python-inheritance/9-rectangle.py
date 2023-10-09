#!/usr/bin/python3
"""Defining a child class of Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defining a class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Defines a class Rectangle that inherits from BaseGeometry
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
         """Return the print() and str() to represent the Rectangle."""
         string = "[" + str(self.__class__.__name__) + "] "
         string += str(self.__width) + "/" + str(self.__height)
         return string
