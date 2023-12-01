#!/usr/bin/python3
#This script posts an email

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = url.parse.urlencode(values)
    data = data.encode('ascii')
    request= urllib.request.Request(data, url)
    with url.request.urlopen(request) as response :
        print(response.read().decode('utf-8'))
