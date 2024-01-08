#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(objct, same_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        objct (any): The object to check.
        same_class (type): The class to match the type of objct to.
    Returns:
        If objct is exactly an instance of same_class - True.
        Otherwise - False.
    """
    if type(objct) == same_class:
        return True
    return False
