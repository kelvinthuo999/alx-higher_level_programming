#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me
url="0.0.0.0:5000/catch_me"; data="user_id=98"; header="Origin:HolbertonSchool"; curl -s -X PUT -L -d "$data" -H "$header" "$url"
