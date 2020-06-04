#!/usr/bin/python3
"""contains Student, to_json"""


class Student:
    """class is in session"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict"""
        lson = {}
        if attrs == None or type(attrs) != list:
            return self.__dict__
        else:
            for item in self.__dict__:
                if item in attrs:
                    lson[item] = self.__dict__[item]
                return lson
