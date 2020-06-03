#!/usr/bin/python3
"""contains append_write"""


def append_write(filename="", text=""):
    """appends string to end of file"""
    with open(filename, 'a') as f:
        return f.write(text)
