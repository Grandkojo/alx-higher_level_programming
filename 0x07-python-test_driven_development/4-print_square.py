#!/usr/bin/python3
"""
	This module contains a function that prints a square with #
"""
def print_square(size):
	"""This funtion prints a square with the character #

	Args:
		size: size of square
	Raises:
		TypeError: if size is not integer
		ValueError: if size is less than zero
		TypeError: if size is a float ad less than zero
	Returns: a square with the character #
	"""
	if not isinstance(size, int):
		raise TypeError("size must be an integer")
	if size < 0:
		raise ValueError("size must be >= 0")
	if isinstance(size, float) and size < 0:
		raise TypeError("size must be an integer")
	for n in range(0, size):
		for m in range(size)
			print('#', end = "")
		print(" ")
