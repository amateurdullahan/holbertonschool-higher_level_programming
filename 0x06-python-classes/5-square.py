#!/usr/bin/python3
"""Documentation for a square class"""


class Square:
    """Square class is 4 sided shape"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if size == 0:
            print()
        else:
            for a in range(self.size):
                for b in range(self.size):
                    print('#', end='')
                print()
