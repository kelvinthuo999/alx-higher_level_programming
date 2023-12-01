#!/usr/bin/python3
"""
Script to send a request to a URL and display the value of X-Request-Id.
"""

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.info()
    x_request_id = headers.get('X-Request-Id')
    print(x_request_id)
