#!/usr/bin/python3

if __name__ == '__main__':
	import sys

	arguments = sys.argv[1:]

	length = 0
	for arg in arguments:
    		length += 1
	print(f"{length} arguments:")

	for i in range(0, length):
    		print(f"{i+1}: {arguments[i]}")
          

