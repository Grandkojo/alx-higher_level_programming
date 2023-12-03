#!/usr/bin/python3
"""This script prints error codes """


import sys
import requests


if __name__ == "__main__":
    request = sys.argv[1]
    url = requests.get(request)
    try:
        url.raise_for_status()
        print(url.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code {e.status_code}")
