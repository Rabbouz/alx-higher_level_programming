#!/usr/bin/python3
def subtract(list_numbers):
    sub = 0
    maximum_list = max(list_numbers)

    for itr in list_numbers:
        if maximum_list > itr:
            sub += itr

    return (maximum_list - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_numbers.keys())

    number = 0
    last_rom = 0
    list_numbers = [0]

    for itr in roman_string:
        for r_num in list_keys:
            if r_num == itr:
                if rom_numbers.get(itr) <= last_rom:
                    num += subtract(list_numbers)
                    list_numbers = [rom_numbers.get(itr)]
                else:
                    list_numbers.append(rom_numbers.get(itr))

                last_rom = rom_numbers.get(itr)

    number += subtract(list_numbers)

    return (number)
