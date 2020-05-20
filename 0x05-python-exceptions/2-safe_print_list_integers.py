#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    b = 0
    a = 0
    if x == 0:
        return a
    else:
        for a in range(x):
            try:
                print("{:d}".format(my_list[a]), end="")
            except (ValueError, TypeError):
                b += 1
                pass
        print()
        return ((a+1) - b)
