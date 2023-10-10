#!/usr/bin/python3
"""Defning a text file(reading) function"""


def write_file(filename="", text=""):
    """Appending a string at the end of text file.

    Args:
        filename (str): the file to write in.
        text (str): The text to be appended in the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
