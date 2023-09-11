#!/usr/bin/python3
"""This module has 2 classes"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ this is a rectangle class"""

    def __init__(self, width, height):
        """the initializor function"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """the string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """REctangle: area of the rectangle"""
        return self.__width * self.__height
