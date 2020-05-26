#!/usr/bin/python3
"""Real Rectangle Class"""


class Rectangle:
    """Defines rectangle"""
    def __init__(self, width=0, height=0):
        """init rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """init width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """init height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
