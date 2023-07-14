#!/usr/bin/python3
"""Creating a square class"""


class Square:
	"""Defining a square class"""
	def __init__(self, size=0):
        	"""Initializing a square class
        	Args: size=0: size of the square
       		"""
		self.__size = size

	@property
	def size(self):
		"""getting the size of the square"""
		return sef.__size
	
	@size.setter
	def size(self, value):
		"""Setting the size of the square"""
        	if type(size is not int:
                	raise TypeError("size must be an integer")
      		if size < 0:
                	raise ValueError("size must be >= 0")
        	self.__size = value
	
	def area(self):
		"""Calculating are of the squarea"""
		return (self.__size ** 2)

	def my_print(self):
		"""Printing the square"""
		if self.__size == 0:
			print()
		else:
			for item in range(self.__size):
				print("#" * self.__size)
