#!/usr/bin/python3
"""contains Student, to_json"""


class Student:
    """class is in session"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict"""
        return self.__dict__
