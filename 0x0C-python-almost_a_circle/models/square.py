#!/usr/bin/python3
"""This module is for a square class that inherits from the rectangle class"""


from .rectangle import Rectangle


class Square:
    """The square class that inherits from the Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """The initializor of the square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of the square"""
        square_name = "[Square] {()} {()}/{()} - {}".format(self.id, self.x, self.y, self.size)
        return square_name

    @property
    def size(self):
        """The getter and setter for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """The update function of the square class"""
        square_attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i == 4:
                    break
        setattr(self, square_attributes[i], arg)

        elif kwargs:
            for key, value in kwargs.items():
                if key in square_attributes:
                    setattr(self, key, value)
