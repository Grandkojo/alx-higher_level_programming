#!/usr/bin/python3
"""THis module checks the list"""


class MyList(list):
    """This is my list class"""

    def __init__(self):
        """This initializes the list"""
        super().__init__()

    def print_sorted(self):
        """THis prints a sorted list"""
        print(sorted(self))
