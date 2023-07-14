#!/usr/bin/python3
""" Creating a rectangle class """


class Rectangle:
	""" Creating a rectangle class """
	def __init__(self, width=0, height=0):
		"""initiating class
		Args: width: width of rectangle
		Args: height: height of rectangle
		"""
		self.__width = width
		self.__height = height

	@property
	def width(self):
		"""Width of rectangle"""
		return (self.__width)

	@width.setter
	def width(self, value):
		"""Sets width of the rectangle to a value"""
		if type(value) is not int:
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property	
	def height(self):
		"""Height of rectangle"""
		return (self.__height)

	@height.setter
	def height(self, value):
		"""Sets height of the rectangle to a value"""
		if type(value) is not int:
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value	
