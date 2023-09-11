#!/usr/bin/python3
"""This module has only one class"""


class BaseGeometry():
    """This class is a geometry class"""

    def area(self):
        """finds the area of the class"""
        raise Exception("area() is not implemented")
   def integer_validator(self, name, value):
        """Validates the arguments"""
        if not isinstance(name, str):
            raise TypeError("{} must be an integer".format(name))
	if value <= 0:
	    raise ValueError("{}  must be greater than 0".format(value))
