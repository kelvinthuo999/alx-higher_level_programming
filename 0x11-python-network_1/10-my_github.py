#!/usr/bin/python3
"""
Use GitHub API to display user id using Basic Authentication with a personal access token.
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

def fetch_github_id(username, password):
    url = 'https://api.github.com/user'
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))

        # Check if the request was successful (status code 2xx)
        response.raise_for_status()

        # Check if the response is in JSON format
        user_data = response.json()

        # Check if 'id' is in the response
        if 'id' in user_data:
            return user_data['id']
        else:
            print("Unable to fetch user id. Check your credentials.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    if len(argv) != 3:
        print("Usage: ./github_id.py <username> <personal_access_token>")
    else:
        username, password = argv[1], argv[2]
        github_id = fetch_github_id(username, password)

        if github_id is not None:
            print("Your GitHub user id is:", github_id)
