#!/usr/bin/python3
"""This module contains a function called lookup """


def lookup(obj):
	"""The lookup function
	Args:
		The object to be received
	Returns:
		A list of all the available attributes and methods of the object
	"""
	return dir(obj)
