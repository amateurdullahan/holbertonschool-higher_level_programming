#!/usr/bin/python3
"""contains load_from_json_file"""
import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename) as f:
        return json.loads(f.readline())
