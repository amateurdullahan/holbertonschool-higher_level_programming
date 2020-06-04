#!/usr/bin/python3
"""add a attry"""


def add_attribute(obj, name, value):
    """adds attribute if possible"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
