#!/usr/bin/python3
"""This module contains classes that perform specific functions"""


class Base:
    """This is the base class defined that manages id"""
    __nb_objects = 0

    def __init__(self, id=None):
    """Class constructor or initializer"""
    if id is not None:
        self.id = id
    else:
       Base. __nb_objects += 1
       self.id = Base.__nb_objects
