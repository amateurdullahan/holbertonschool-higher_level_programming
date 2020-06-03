#!/usr/bin/python3
"""contains number_of_lines"""


def number_of_lines(filename=""):
    """return number of lines of file"""
    c = 0
    with open(filename) as f:
        for r in f:
            c += 1
        return(c)
