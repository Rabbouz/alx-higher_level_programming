#!/usr/bin/python3
"""Defning a text file(reading) function"""


def write_file(filename="", text=""):
    """ Writing a string to a text file (UTF8)
    and returns the number of characters written.
    
    Args:
    filename: the file to be write in.
    text(str): the text to be written
    """
    with open(filename,"w", encoding="utf-8") as f:
        return f.write(text)
