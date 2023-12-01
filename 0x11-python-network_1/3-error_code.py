#!/usr/bin/python3
"""This script prints error codes """


import sys
import urllib.request


if __name__ == "__main__":
    request = sys.argv[1]
    try:
        with urllib.request.urlopen(request) as response:
            html = response.read()
            print(html)
    except urllib.error.URLError as e:
        print(e.reason)
