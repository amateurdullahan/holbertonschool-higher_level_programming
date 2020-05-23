#!/usr/bin/python3
"""Functio to print a square"""


def print_square(size):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        for b in range(size):
            print('#', end="")
        print()
