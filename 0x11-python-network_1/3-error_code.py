#!/usr/bin/python3
"""
script to take url, send request
to the url and display the value
of X-Request-Id found in the
header
"""
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
