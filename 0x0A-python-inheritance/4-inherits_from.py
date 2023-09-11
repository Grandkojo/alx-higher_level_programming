#!/usr/bin/python3
"""This module has one function"""


def inherits_from(obj, a_class):
    """checks inheritance of an obj either(directly or not directly)"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class

