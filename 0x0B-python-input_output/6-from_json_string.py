#!/usr/bin/python3
"""contains from_json_string"""
import json


def from_json_string(my_str):
    """returns obj represented by JSON"""
    return json.loads(my_str)
