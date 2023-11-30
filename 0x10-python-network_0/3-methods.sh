#!/bin/bash
# This script sends an OPTIONS request to a URL and displays the allowed HTTP methods
curl -s -i -X OPTIONS "$1" | grep -i allow | cut -d " " -f 2-
