#!/usr/bin/python3
"""Rectangle Class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangles!"""
    def __init__(self, width, height):
        """init of Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string method"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
