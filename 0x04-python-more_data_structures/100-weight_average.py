#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or type(my_list) is not list or len(my_list) == 0:
        return 0
    wait = 0
    scar = 0
    for a in my_list:
        wait += a[1]
        scar += (a[0] * a[1])
    return (scar / wait)
