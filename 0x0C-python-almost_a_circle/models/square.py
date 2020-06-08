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
