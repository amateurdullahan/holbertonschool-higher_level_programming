#!/usr/bin/python3
"""Base file"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base init"""
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
