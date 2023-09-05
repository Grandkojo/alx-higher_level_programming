#!/usr/bin/python3
"""
	This module contains one function that prints text indentations according to special characters
"""
def text_indentation(text):
	"""This function prints a text with 2 new lines after each of these characters: ., ? and :
	Args:
		text: only argument, a string
	Raises:
		TypeError: if the argument is not a string
	Returns:
		A new line with a set of strings in the argument
	"""
	if not isintance(text, str):
		raise TypeError("text must be a string")

	count = 0
	while count < len(text) and text[count] == " ":
        	count = count + 1

    	while count < len(text):
        	print(text[count], end="")
        	if text[count] == "\n" or text[count] in ".?:":
            		if text[count] in ".?:":
                		print("\n")
            		count = count + 1
            		while count < len(text) and text[count] == " ":
                		count = count + 1
            		continue
        	count = count + 1
