#!/usr/bin/python3
"""Defining a square-printing function."""


def print_square(size):
    """Printing a square with the # character.

    Args:
        size: The height & width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for itr in range(size):
        [print("#", end="") for j in range(size)]
        print("")
