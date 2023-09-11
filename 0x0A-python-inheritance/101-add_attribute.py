#!/usr/bin/python3
"""this imodule adds an atrribute"""


def add_attribute(obj, attr, value):
    """adds an attribute to an obj"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
