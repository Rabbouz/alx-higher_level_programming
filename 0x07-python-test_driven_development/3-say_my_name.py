#!/usr/bin/python3
"""Defining a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Printing a name.

    Args:
        first_name: The first name to be printed.
        last_name: The last name to be printed.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
