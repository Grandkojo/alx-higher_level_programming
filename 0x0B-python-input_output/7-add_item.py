#!/usr/bin/python3
"""This module adds an item to a list"""


import json
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


fname = 'add_item.json'
if os.path.exists(fname):
    my_list = load_from_json_file(fname)
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, fname)
