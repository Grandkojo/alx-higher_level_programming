#/bin/bash
#Prints the size of a content in bits
curl -s "$1" | wc -c
