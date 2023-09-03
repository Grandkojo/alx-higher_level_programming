#!/usr/bin/python3
"""
	This module contains one function that prints a person's full name
"""

def say_my_name(first_name, last_name=""):
	""" A function that prints a person's first name and last name
	Args:
		first_name: first argument
		last_name: second argument
	Returns:
		 A string that contains the person's first name and last name
	Raises:
		TypeError: if any of the arguments is not a string
	"""
	if ((not isinstance(first_name, str)):
		raise TypeError("first_name must be a string")
	if ((not isinstance(last_name, str)):
		raise TypeError("last_name must be a string")
	print(f"My name is {first_name} {last_name}")

