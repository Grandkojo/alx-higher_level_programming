#!/usr/bin/python3
"""THis is a rectangle class"""


class Rectangle:
    """This is a rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """the setter and getter for the with"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """The string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        res = '\n'.join([str(self.print_symbol) * self.width
                         for i in range(self.height)])
        return res

    def __repr__(self):
        """returns a representation of the rectangle
        that can be evaluated"""
        res = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return res

    def __del__(self):
        """the delete magic method"""
        print("Bye rectangle...")
        if Rectangle.number_of_instances != 0:
            Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """check for the bigger rectangle"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
