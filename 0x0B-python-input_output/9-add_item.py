#!/usr/bin/python3
"""9-add_item"""
from sys import argv



save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    filename = "add_item.json"
    json_list = load_from_json_file(filename)
except:
    json_list = []

for c in range(1, len(argv)):
    json_list.append(argv[c])

save_to_json_file(json_list, filename)
