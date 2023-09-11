#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult = []
    for itr in range(len(my_list)):
        if my_list[itr] % 2 == 0:
            mult.append(True)
        else:
            mult.append(False)
    return (mult)
