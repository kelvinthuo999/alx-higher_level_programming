#!/usr/bin/python3
"""
Script to send a request to a URL and display the response body.
Prints an error message if the HTTP status code is >= or == to 400.
"""

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./7-error_code.py <URL>")
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)

if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response.text)
