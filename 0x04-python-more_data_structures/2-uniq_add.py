#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_lst = set(my_list)
    num = 0

    for itr in uniq_lst:
        num += itr
    return (num)
