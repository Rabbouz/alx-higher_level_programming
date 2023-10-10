#!/usr/bin/python3
"""Defning a text file(reading) function"""


def read_file(filename=""):
    """Reading the file text 'UTF8' and printing it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
