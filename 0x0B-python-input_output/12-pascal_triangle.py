#!/usr/bin/python3
"""This is the pascal triangle module"""


def pascal_triangle(n):
    """This function returns a list of pascal triangle"""
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    res = [[1], [1, 1]]
    for i in range(1, n - 1):
        n = [1, 1]
        for j in range(len(res[i]) - 1):
            n.insert(-1, res[i][j] + res[i][j + 1])
        res.append(n)
    return res
