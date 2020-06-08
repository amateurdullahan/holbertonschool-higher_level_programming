#!/usr/bin/python3
"""Square file"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """init square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overwritten str"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """get size, which is width"""
        return self.width

    @size.setter
    def size(self, size):
        """set width and height to same value"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be >= 0")
        self.__width = size
        self.__height = size
