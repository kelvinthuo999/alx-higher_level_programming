#!/usr/bin/python3
"""
Send a POST request with a letter as a parameter.
"""

import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

data = {'q': q}

try:
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    json_data = response.json()

    if json_data:
        print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    else:
        print("No result")

except ValueError:
    print("Not a valid JSON")
except requests.exceptions.RequestException as e:
    print("Error:", e)
