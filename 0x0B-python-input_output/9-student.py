#!/usr/bin/python3
"""This modules has a functino called student_to_json"""


class Student():
    """This is the student class"""
    def __init__(self, first_name, last_name, age):
        """The student class initializor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This function converts the student class to json representation"""
        jsonrepr = {j: v for j, v in self.__dict__().items() if not j.startswith("__")}
        return jsonrepr
