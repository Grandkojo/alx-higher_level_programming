#!/usr/bin/python3
"""This module contains a fucntin that returns an object from json string"""


import json


def from_json_string(my_obj):
    """This function reutrns an object from json string"""
    if my_obj is None:
        return
    return json.loads(my_obj)
