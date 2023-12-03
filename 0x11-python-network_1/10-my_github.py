#!/usr/bin/python3
"""This script uses github api to display my id"""

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    html = requests.get(url, auth=(username, password))
    response = html.json()
    print(response.get('id'))
