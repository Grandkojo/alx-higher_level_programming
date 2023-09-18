#!/usr/bin/python3
"""This module has one class that inherits from base"""


from .base import Base


class Rectangle(Base):
    """This is the Rectangle class that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The initializer or constructor function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The setter and getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The setter and getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The setter and getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The setter and getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """The area of the Rectangle instance"""
        return self.height * self.width

    def display(self):
        """Prints the Rectangle with #"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """String representation of Rectangle instance"""
        rect_name = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
        return rect_name

    def update(self, *args, **kwargs):
        """The update method of the Rectangle"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i == 5:
                    break
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """The dictionary representation of the Rectangle class"""
        dict_rep = {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
        return dict_rep

