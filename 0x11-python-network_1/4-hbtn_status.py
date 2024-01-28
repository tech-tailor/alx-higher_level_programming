#!/usr/bin/python3
"""
script to take url, send request
to the url and display the value
of X-Request-Id found in the
header
"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    body = r.content.decode()
    print('Body response:')
    print('\t- type:', type(body))
    print('\t- content:', body)
