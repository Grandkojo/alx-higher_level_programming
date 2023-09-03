#!/usr/bin/python3
"""
	This module has one function that adds two integers
"""
def add_integer(a, b=98):
	""" Addition function that adds two integers or floats
	Args:
		a: first argument
		b: second argument
	Returns:
		Sum of two arguments
	Raises:
		TypeError: if any of the arguments is not an integer or float
	"""
	if ((not isinstance(a, int) and not isinstance(a, float)))
		raise TypeError("a must be an integer")
	if ((not isinstance(b, int) and not isinstance(b, float)))
		raise TypeError("b must be an ineger")
	return (int(a) + int(b))
