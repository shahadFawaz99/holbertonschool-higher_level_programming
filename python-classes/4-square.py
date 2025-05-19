#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size (int): The size of the square (default is 0)
        """
        self.size = size  # استخدم setter هنا مباشرة

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
