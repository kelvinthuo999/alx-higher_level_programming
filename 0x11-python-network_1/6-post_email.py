#!/usr/bin/python3
"""
Send a POST request with an email parameter and display the response body.
"""

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./6-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)

print(response.text)
