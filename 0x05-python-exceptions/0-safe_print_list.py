#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    if x == 0:
        return a
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
        except IndexError:
            print()
            return a
    print()
    return a+1
