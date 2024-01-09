#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trnal = triangles[-1]
        tm = [1]
        for i in range(len(trnal) - 1):
            tm.append(trnal[i] + trnal[i + 1])
        tm.append(1)
        triangles.append(tm)
    return triangles
