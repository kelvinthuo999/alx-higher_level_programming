#!/usr/bin/python3
"""
Use GitHub API to display user id using Basic Authentication with a personal access token.
"""

import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./github_id.py <kelvinthuo999> <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>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

url = "https://api.github.com/user"

# Set up the authentication using Basic Authentication with personal access token
auth = (username, token)

try:
    response = requests.get(url, auth=auth)
    user_data = response.json()

    if 'id' in user_data:
        print("Your GitHub user id is:", user_data['id'])
    else:
        print("Unable to fetch user id. Check your credentials.")

except ValueError:
    print("Not a valid JSON")
except requests.exceptions.RequestException as e:
    print("Error:", e)
