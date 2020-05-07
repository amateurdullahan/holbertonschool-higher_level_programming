#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq_list = list(set(my_list))
    for a in range(len(uniq_list)):
        sum += uniq_list[a]
    return sum
