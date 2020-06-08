#!/usr/bin/python3
"""Rectangle file"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle init"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("x", x)
        self.integer_validator("y", y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """init width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set height"""
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """init height"""
        return self.__width

    @height.setter
    def height(self, value):
        """set height"""
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """set x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def integer_validator(self, name, value):
        """validate integer"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))

    def area(self):
        """return area"""
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
        return "[Rectange] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
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
