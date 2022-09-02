#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

from cgitb import html
from urllib import request

with request.urlopen("https://intranet.hbtn.io/status") as response:
    html = response.read()
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('utf8'))
