#!/usr/bin/python3
"""qwerty"""
import urllib.request
import sys


req = urllib.request.Request(sys.argv[1])
try:
    urllib.request.urlopen(req)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)
except urllib.error.HTTPError as err:
    print("Error code: {}".format(err.code))
