#!/usr/bin/python3
""" Python script using header to find a variable """

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    html = requests.get(url)
    print(html.headers.get("X-Request-Id"))
