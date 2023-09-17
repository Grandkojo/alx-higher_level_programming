#!/usr/bin/python3
"""This module is for a square class that inherits from the rectangle class"""


from .rectangle import Rectangle


class Square:
    """The square class that inherits from the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """The initalizor of the square class"""
