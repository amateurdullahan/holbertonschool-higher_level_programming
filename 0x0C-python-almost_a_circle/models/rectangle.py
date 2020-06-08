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
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def integer_validator(self, name, value):
        """validate integer"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))

    def area(self):
        return self.__width * self.__height
