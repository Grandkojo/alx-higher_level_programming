#!/usr/bin/python3
""" This scriot is a search API"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
        load = {'q': q}
        html = requests.post(url, data=load)
        try:
            jsonrep = html.json()
            if jsonrep:
                print(f"[{jsonrep.get('id')}] {jsonrep.get('name')}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
