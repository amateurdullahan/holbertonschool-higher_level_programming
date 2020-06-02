#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    """returns list of all available attributes and methods of object"""
    return list(dir(obj))
