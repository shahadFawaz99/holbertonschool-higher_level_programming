#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initialize a new Square

        Args:
            size (int): The size of the square (default 0)
        """
        self.size = size

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

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
