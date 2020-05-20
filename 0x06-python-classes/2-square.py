#!/usr/bin/python3
"""Documentation for a square class"""


class Square:
    """Square class is 4 sided shape"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
