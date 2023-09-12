#!/usr/bin/python3
"""This module contains a function that loads a json file"""


def load_from_json_file(filename):
    """This func loads a json file"""
    import json
    if filename is None or type(filename) is not str:
        return
    a = None
    with open(filename, "r") as f:
        a = json.JSONDecoder().decode(f.read())
    return a
