#!/usr/bin/python3
"""include save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'a') as f:
        f.write(json.dumps(my_obj))
