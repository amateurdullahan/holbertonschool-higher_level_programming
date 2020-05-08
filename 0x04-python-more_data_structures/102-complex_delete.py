#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = list(a_dictionary.keys())
    for a in key:
        if a_dictionary[a] == value:
            del a_dictionary[a]
    return a_dictionary
