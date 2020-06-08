#!/usr/bin/python3
"""Rectangle file"""
Base = __import__('base').Base


class Rectangle(Base):
    """Rectangle Class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle init"""
        self.id = super().__init__(id=None)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """init width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set height"""
        self.__width = value

    @property
    def height(self):
        """init height"""
        return self.__width

    @height.setter
    def height(self, value):
        """set height"""
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
