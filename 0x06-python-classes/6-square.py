#!/usr/bin/python3
"""Documentation for a square class"""


class Square:
    """Square class is 4 sided shape"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        if self.__position[0] >= 0 and self.__position[1] >= 0:
            for height in range(self.__position[1]):
                print()

        for a in range(self.__size):
            for b in range(self.__position[0]):
                print(' ', end='')
            for c in range(self.__size):
                print('#', end='')
            print()
