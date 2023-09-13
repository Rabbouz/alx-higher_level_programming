#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst_ord = list(a_dictionary.keys())
    lst_ord.sort()
    for itr in lst_ord:
        print("{}: {}".format(itr, a_dictionary.get(itr)))
