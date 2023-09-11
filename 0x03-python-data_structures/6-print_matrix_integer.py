#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for collum in row:
            print("{:d}".format(collum), end=" " if collum != row[-1] else "")
        print()
