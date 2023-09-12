#!/usr/bin/python3
"""This modules has a functin that save an object to json"""


def save_to_json_file(my_obj, filename):
    """This function saves to ajson file"""
    import json
    if filename is None or type(filename) is not str:
        return
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.JSONEncoder().encode(my_obj))
