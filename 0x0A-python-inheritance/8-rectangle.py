#!/usr/bin/python3
"""Defining a child class of Rectangle."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Represent a rectangle from BaseGeometry"""
    def __init__(self, width, height):
        """Intializing a new child Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
