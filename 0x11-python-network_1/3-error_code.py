#!/usr/bin/python3
"""This script prints error codes """


import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    request = sys.argv[1]
    url = urllib.request.Requezt(url)
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error code: {e.reason}")
