#!/bin/usr/python3
"""Class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class!"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.size = size
        super().__init__(size, size)
