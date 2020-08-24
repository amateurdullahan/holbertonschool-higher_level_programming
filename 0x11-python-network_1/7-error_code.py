#!/usr/bin/python3
"""perror"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    try:
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(req.status_code))
