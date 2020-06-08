#!/usr/bin/python3
"""Base file"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return dump"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write json representation to file"""
        nlist = []
        for obj in list_objs:
            nlist.append(obj.to_dictionary())
        nstr = (cls.to_json_string(nlist))
        fname = "{}.json".format(cls.__name__)
        with open(fname, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(nstr)

    def from_json_string(json_string):
        """return list of json string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
