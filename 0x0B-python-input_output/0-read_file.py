#!/usr/bin/python3
"""contains read_file"""


def read_file(filename=""):
    """method to read file"""
    with open(filename) as f:
        print(f.read(), end="")
