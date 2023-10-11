#!/usr/bin/python3
"""Defining a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserting text after each line containing a given string in a file.

    Args:
        filename(string): The name of the file.
        search_string(string): The string to search for within the file.
        new_string(string): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
