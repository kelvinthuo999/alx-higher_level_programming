#!/usr/bin/python3
"""
Script to fetch https://alx-intranet.hbtn.io/status using urllib.
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()

print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content.decode('utf-8'))
