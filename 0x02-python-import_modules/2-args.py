#!/usr/bin/python3

if __name__ == '__main__':
	import sys

	arguments = sys.argv[1:]

	length = 0
	for arg in arguments:
    		length += 1
	if length == 0:
		print("0 arguments")
	elif length == 1:
		print("1 argument")
	else:	
		print(f"{length} arguments:")

	for i in range(0, length):
    		print(f"{i+1}: {arguments[i]}")
