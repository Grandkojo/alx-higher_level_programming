#!/usr/bin/python3
"""This module contains one function that converts to JSON"""


import json


def to_json_string(my_obj):
    """This function converts the string to JSON string"""
    if my_obj is None:
        return
    print(json.dumps(my_obj))
