#!/usr/bin/python3
"""Square file"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init square"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overwritten str"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set width and height to same value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        self.__height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """update square"""
        udict = {0: self.id, 1: self.size, 2: self.x, 3: self.y}
        if args:
            for c, update in enumerate(args):
                udict[c] = update
                self.id, self.size, self.x, self.y = (
                udict[0], udict[1], udict[2], udict[3])
        else:
            for key, update in kwargs.items():
                setattr(self, key, update)

    def to_dictionary(self):
        """return dictionary"""
        squ_dict = {'id': self.id, 'size': self.__size, 'x': self.x,
                    'y': self.y}
        return squ_dict
