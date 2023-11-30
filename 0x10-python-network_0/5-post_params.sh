#!/bin/bash
# This script is used to post parameters
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
