#!/usr/bin/python3
"""This module defines an rectangle class."""

class Rectangle:
	"""An rectangle class"""

	def _int__(self, width=0, height=0):
	"""Initialize a rectangle
	Args:
		width(int): width of rectangle
		height(int): height of rectangle
	"""
	self.width = width
	self.height = height

	@property
	def witdh(self):
		"""Get the width of the rectangle"""
		return self.__width

	@width.setter
	def width(self, value):
		if not isinstance (value, int):
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
                """Get the height of the rectangle"""
                return self.__height

        @height.setter
        def height(self, value):
                if not isinstance (value, int):
                        raise TypeError("height must be an integer")
                if value < 0:
                        raise ValueError("height must be >= 0")
		self.__height = value
