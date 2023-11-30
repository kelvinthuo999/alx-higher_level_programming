#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response if the status code is 200
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
