#!/usr/bin/python3
"""
Module that defines a Square class inheriting from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize Square with size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        String representation of Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
