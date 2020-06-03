#!/usr/bin/python3
"""contains read_lines"""


def read_lines(filename="", nb_lines=0):
    """return number of lines of file"""
    c = 0
    with open(filename) as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            while c < nb_lines:
                print(f.readline(), end="")
                c += 1
