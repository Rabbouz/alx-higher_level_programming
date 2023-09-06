#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    """"Printing the the ASCII alphabet in reverse
    order alternating lower- and uppercase"""
    if c % 2 == 0:
        print("{}".format(chr(c).lower()), end="")
    else:
        print("{}".format(chr(c).upper()), end="")
