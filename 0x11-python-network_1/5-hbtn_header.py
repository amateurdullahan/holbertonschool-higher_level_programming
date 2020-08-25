#!/usr/bin/python3
"""porsche"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    ret = req.headers.get('X-Request-Id')
    print(ret)
