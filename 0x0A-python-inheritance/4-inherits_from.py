#!/usr/bin/python3
"""This module contains only one function"""


def is_same_class(obj, a_class):
    """Checks if the object is an instance of a class that inherited from the specified class"""
    return issubclass(obj, a_class)
