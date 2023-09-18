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
            Base.__nb_objects += 1
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
                for obj in list_objs:
                    list_dictionary.append(obj.to_dictionary())
            f.write(cls.to_json_string(list_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the json string representation"""
        import json
        if json_string is None:
            return []
        else:
            return json.JSONDecoder().decode(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This creates a new instance of the calling class"""
        temp = None
        if cls.__name__ == "Rectangle":
            temp = cls(2, 3)
        elif cls.__name__ == "Square":
            temp = cls(4)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a file"""
        filename = cls.__name__ + ".json"
        try:
            res = []
            with open(filename, "r") as f:
                list_dict = cls.from_json_string(f.read())
                for dic in list_dict:
                    res.append(cls.create(**dic))
                return res
        except Exception:
            return []

