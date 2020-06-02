#!/usr/bin/python3
"""inheritance func"""


def inherits_from(obj, a_class):
    """checks inheritance of obj"""
    return issubclass(type(obj), a_class) and (type(obj) is not a_class)
