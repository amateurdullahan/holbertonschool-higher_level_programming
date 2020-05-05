#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if not my_list:
        return None
    for a in range(len(my_list)):
        if my_list[a] > max:
            max = my_list[a]
    return max
