#!/usr/bin/python3
"""comorant"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        ri = response.getheader('X-Request-Id')
        print(ri)
