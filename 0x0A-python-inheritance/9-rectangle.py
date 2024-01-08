#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, w, h):
        """Intialize a new Rectangle.

        Args:
            w (int): The width of the new Rectangle.
            h (int): The height of the new Rectangle.
        """
        super().integer_validator("width", w)
        self.__width = w
        super().integer_validator("height", h)
        self.__height = h

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        s = "[" + str(self.__class__.__name__) + "] "
        s += str(self.__width) + "/" + str(self.__height)
        return s
