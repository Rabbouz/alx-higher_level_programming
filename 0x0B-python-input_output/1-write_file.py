#!/usr/bin/python3
"""Defning a text file(reading) function"""


def write_file(filename="", text=""):
    """Writing a string to a UTF8 text file.

    Args:
        filename (str): the file to write in.
        text (str): The text to be written in the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
