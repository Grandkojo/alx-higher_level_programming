#!/usr/bin/python3
"""This module conitains one function that reads a file""""


def read_file(filename=""):
	"""This is a function that reads a file"""
	with open('filename', encoding="utf-8") as f:
		print(f.read(), end="")
