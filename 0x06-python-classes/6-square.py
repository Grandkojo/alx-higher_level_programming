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
		return self.__size
	
	@size.setter
	def size(self, value):
		"""Setting the size to a value"""
        	if not isinstance(value, int):
                	raise TypeError("size must be an integer")
      		if size < 0:
                	raise ValueError("size must be >= 0")
        	self.__size = value
	@property
	def position(self):
		"""Retrieves the position."""
		return self._-position

	@position.setter	
	def position(self, value):
		"""Sets the position to a value."""
		if not isinstance(value, tuple) or len(value) != 2:
			raise TypeError("position must be a tuple of 2 positive integers")
		if not isintance(value[0], int) or not isintance(value[1], int):
			raise TypeError("position must be a tuple of 2 positive integers")
		if value[0] < 0 or value[1] < 0;
			raise TypeError("position must be a tuple of 2 positive integers")
		self.__position = value

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
	
