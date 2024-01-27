#!/usr/bin/python3
"""
script to take url, send request
to the url and display the value
of X-Request-Id found in the
header
"""
import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email':  sys.argv[2]}
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
