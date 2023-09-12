#!/usr/bin/python3
"""This module contains one function that writes to a file."""


def write_file(filename="", text=""):
    """This function writes to a file."""
    with open(filename, 'w', encoding="utf-8") as f:
        written = f.write(text)
    return written
