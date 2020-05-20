#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    for a in range(x):
        try:
            print("{}".format(my_list[a]), end="")
            printed += 1
        except IndexError:
            break
    if printed != 0:
        print()
    return printed
