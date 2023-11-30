#!/bin/bash
# This scrip is used to get all the http methods of a server
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f 2-
