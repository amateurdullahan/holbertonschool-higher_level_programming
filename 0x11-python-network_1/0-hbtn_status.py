#!/usr/bin/python3
"""comment"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    typo = type(response.read())
    decode = html.decode(encoding='UTF-8')
    print("Body response:\n\t- type: {}\n\t- content: \
{}\n\t- utf8 content: {}".format(typo, html, decode))
