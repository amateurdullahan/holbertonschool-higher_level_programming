#!/usr/bin/python3
"""Real Rectangle Class"""


class Rectangle:
    number_of_instances = 0

    """init rectangle"""
    def __init__(self, width=0, height=0):
        """init rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """find area"""
        return (self.height * self.width)

    def perimeter(self):
        """find perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return ((self.height * 2) + (self.width * 2))

    def __str__(self):
        """print rectangle"""
        rect = ""
        if self.width == 0 or self.height == 0:
            return rect
        for a in range(self.height):
            rect += ('#' * self.width)
            if a + 1 != self.height:
                rect += '\n'
        return rect

    def __repr__(self):
        """string rep"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """print message with delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
