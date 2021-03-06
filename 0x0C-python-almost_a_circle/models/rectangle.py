#!/usr/bin/python3
"""Rectangle file"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes all attributes. """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Height of the rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def y(self):
        """ Y position of the rectangle. """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """ X position of the rectangle. """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """ Calculates the area of the rectangle. """
        return self.__width * self.__height

    def display(self):
        """prints rectangle"""
        for a in range(self.__y):
            print()
        for b in range(self.__height):
            print(" " * self.__x, end='')
            for d in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """class specific str method"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update"""
        udict = {0: self.id, 1: self.__width,
                 2: self.__height, 3: self.__x, 4: self.__y}
        if args:
            for c, update in enumerate(args):
                udict[c] = update
            self.id, self.__width, self.__height, self.__x, self.__y = (
                udict[0], udict[1], udict[2], udict[3], udict[4])
        else:
            for key, update in kwargs.items():
                setattr(self, key, update)

    def to_dictionary(self):
        """to dictionary"""
        rec_dict = {'x': self.__x, 'y': self.__y, 'id': self.id,
                    'height': self.__height, 'width': self.__width}
        return rec_dict
