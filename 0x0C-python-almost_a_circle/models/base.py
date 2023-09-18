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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Represent the json representation"""
        import json
        if list_dictionaries is None:
            return "[]"
        else:
            return json.JSONEncoder().encode(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the json representation of @list_objs to a file"""
        import json
        with open(f'{cls.__name__}.json', 'w') as f:
            list_dictionary = []
            if list_objs:
                for obj n list_objs:
                    list_dictionary.append(obj.to_dictionary())
            f.write(cls.to_json_string(list_dictionary))
