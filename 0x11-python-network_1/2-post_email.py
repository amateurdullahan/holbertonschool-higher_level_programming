#!/usr/bin/python3
"""baron"""
import urllib.request
import urllib.parse
import sys

value = {'email': sys.argv[2]}
data = urllib.parse.urlencode(value)
data = data.encode('utf-8')
req = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(req) as response:
    html = response.read().decode(encoding='UTF-8')
    print(html)
