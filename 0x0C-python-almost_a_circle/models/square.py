#!/usr/bin/python3
"""This module is for a Square class that inherits from the Rectangle class"""


from .rectangle import Rectangle


class Square(Rectangle):
    """The Square class that inherits from the Rectangle class"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """The initializer of the Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the Square"""
        square_name = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
        return square_name

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update function of the Square class"""
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

    def to_dictionary(self):
        """Dictionary representation of the Square"""
        dict_rep = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dict_rep

