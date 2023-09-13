#/usr/bin/python3
"""This module contains a function that returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """This function converts a class to a json string"""
    jsonrepr = {j: v for j, v in obj.__dict__.items() if not k.startswith("__")}
    return (jsonrepr)
