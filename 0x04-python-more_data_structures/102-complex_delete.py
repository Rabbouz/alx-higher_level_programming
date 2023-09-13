#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())
    for v_dict in list_keys:
        if value == a_dictionary.get(v_dict):
            del a_dictionary[v_dict]

    return (a_dictionary)
