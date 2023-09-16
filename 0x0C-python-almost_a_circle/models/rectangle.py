#!/usr/bin/python3
"""This modules has one class that inherits from base"""


from .base import Base


class Rectangle(Base):
    """This is the rectangle class that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The iitializer or constructor function"""
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
            raise TypeError("width must be integer")
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
            raise TypeError("height must be integer")
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
            raise TypeError("x must be integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.___x = value

    @property
    def y(self):
        """The setter and getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.___y = value

    def area(self):
        """The area of the rectangle instance"""
        return (self.height * self.width)

    def display(self):
        """Prints the rectangle with #"""
        print("\n" * self.y, end="") 
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)
    def __str__(self):
        """string representation of rectangle instance"""
        rect_name = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width,        self.height)
