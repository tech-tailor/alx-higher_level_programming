#!/usr/bin/python3
"""
script to take url, send request
to the url and display the value
of X-Request-Id found in the
header
"""

import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    body = response.headers
    print(body.get('X-Request-Id'))
