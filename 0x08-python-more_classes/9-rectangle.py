#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, w=0, h=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        type(self).number_of_instances += 1
        self.width = w
        self.height = h

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self.__height = val

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rectangle_1, rectangle_2):
        """Return the Rectangle with the greater area.

        Args:
            rectangle_1 (Rectangle): The first Rectangle.
            rectangle_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rectangle_1 or rectangle_2 is not a Rectangle.
        """
        if not isinstance(rectangle_1, Rectangle):
            raise TypeError("rectangle_1 must be an instance of Rectangle")
        if not isinstance(rectangle_2, Rectangle):
            raise TypeError("rectangle_2 must be an instance of Rectangle")
        if rectangle_1.area() >= rectangle_2.area():
            return (rectangle_1)
        return (rectangle_2)


    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recten = []
        for i in range(self.__height):
            [recten.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                recten.append("\n")
        return ("".join(recten))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        recten = "Rectangle(" + str(self.__width)
        recten += ", " + str(self.__height) + ")"
        return (recten)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
