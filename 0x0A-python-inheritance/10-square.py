#!/usr/bin/python3
"""Class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class!"""
    def __init__(self, size):
        """init square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
