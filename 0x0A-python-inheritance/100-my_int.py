#!/usr/bin/python3
"""This is my int"""


class MyInt(int):
    """Personal integer class"""

    def __eq__(self, other):
        """the equals sign"""
        return int(self) != int(other)

    def __ne__(self, other):
        """the not equals sign"""
        return int(self) == int(other)
