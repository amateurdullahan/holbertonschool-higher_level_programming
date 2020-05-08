#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    key = list(a_dictionary.keys())
    best = key[0]
    for a in key:
        if a_dictionary[a] > a_dictionary[best]:
            best = a
    return best
