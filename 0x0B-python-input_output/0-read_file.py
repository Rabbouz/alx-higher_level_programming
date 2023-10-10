#!/usr/bin/python3
"""Reading the file text 'UTF8' and printing it to stdout"""

def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
