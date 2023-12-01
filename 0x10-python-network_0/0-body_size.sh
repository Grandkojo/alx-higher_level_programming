#!/bin/bash
# This script checks the length of the body
curl -s "$1" | wc -c
