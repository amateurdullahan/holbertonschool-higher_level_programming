#!/usr/bin/python3
"""9-add_item"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    json_list = load_from_json_file("add_item.json")
except:
    json_list = []

for c in range(1, len(sys.argv)):
    json_list.append(argv[c])

save_to_json_file(json_list, "add_item.json")
