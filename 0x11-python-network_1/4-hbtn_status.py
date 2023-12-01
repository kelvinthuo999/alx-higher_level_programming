#!/usr/bin/python3
"""
Script to fetch https://alx-intranet.hbtn.io/status using the requests library.
"""

import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)
