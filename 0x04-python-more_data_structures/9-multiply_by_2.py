#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dirc = a_dictionary.copy()
    list_keys = list(new_dirc.keys())

    for itr in list_keys:
        new_dirc[itr] *= 2

    return (new_dirc)
