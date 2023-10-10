#!/usr/bin/python3
"""Defining a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Representing a square."""

def __init__(self, size):
    """Initializing of square.
    
    Args:
    size (int): The size of the new square.
    """
    self.size = ("size", size)
    self.integer_validator("size", size)
    self.__size = size
    