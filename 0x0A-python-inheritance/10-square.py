#!/usr/bin/python3
"""This is the square module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The squre class"""

    def __init__(self, size):
        """initatiates a square"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of the square"""
        return self.__size * self.__size
