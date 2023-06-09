#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    arguments = sys.argv[1:]

    length = 0

    for arg in arguments:
        length = length + int(arg)
    print(length)
