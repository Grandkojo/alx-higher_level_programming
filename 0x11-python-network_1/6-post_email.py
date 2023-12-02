#!/usr/bin/python3
""" #This script posts an email """

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    html = requests.post(url, data=values)
    print(html.text)
