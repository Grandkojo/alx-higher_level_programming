#!/usr/bin/python3
"""
	This module contains one function that divides all elements in a matrix
"""
def matrix_divided(matrix, div):
	"""Divides all elements in a matrix
	Args:
		matrix: first argument, matrix
		div: second argument, divisor
	Returns:
		A divided matrix
	Raises:
		TypeError: if matrix is not a list of lists of interers or floats.
		TypeError: if each row of the matrix is of different sizes.
		TypeError: if div is not an integer of float.
		ZeroDivisionError: if div equals 0.
	"""
	if (not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix or 
	not all(isinstance(element, int) or isinstance(element, float)  for element in [num for row in matrix 
	for num in row]))):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

	if not all(len(row) == len(matrix[0]) for row in matrix):
		raise TypeError("Each row of the matrix must have the same size")

	if not isinstance(div, int) or isinstance(div, float):
		raise TypeError("div must be a number")

	if div == 0:
		raise ZeroDivisionError("div must be zero")
	return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
