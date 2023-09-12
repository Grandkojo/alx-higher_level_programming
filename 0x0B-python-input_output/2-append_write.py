#!/usr/bin/python3
"""This module contains one function that appends unto a file"""


def append_write(filename="", text=""):
    """This function appends unto the file"""
    if filename is None or type(filename) is not str:
        return
    with open(filename, 'a', encoding="utf-8") as f:
        appended = f.write(text)
    return appended
