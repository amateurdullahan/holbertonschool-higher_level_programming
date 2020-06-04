#!/usr/bin/python3
"""contains append_after"""


def append_after(filename="", search_string="", new_string=""):
    """insert new string after search string"""
    with open(filename) as fr:
        readr = fr.readlines()
    c = 0
    with open(filename, 'w') as fw:
        for lines in readr:
            c += 1
            if search_string in lines:
                readr.insert(c, new_string)
        for lines in readr:
            fw.write(lines)
