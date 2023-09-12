#!/usr/bin/python3
"""This module contains a function that creates an object from JSON file"""


def load_from_json_file(filename):
    """This function creates an object from JSON"""
    import json
    if filename is None or type(filename) is not str:
        return
    with open(filename, 'r', encoding="utf-8"):
        read = json.JSONEncoder().decode(f.read())
    return read
