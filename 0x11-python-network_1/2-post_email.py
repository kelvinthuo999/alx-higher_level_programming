#!/usr/bin/python3
"""
Send a POST request with an email parameter and display the response body.
"""

import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
request = urllib.request.Request(url, data=data, method='POST')

with urllib.request.urlopen(request) as response:
    content = response.read().decode('utf-8')
    print(content)
