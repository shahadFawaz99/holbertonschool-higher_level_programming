#!/usr/bin/python3
"""Defines a class Square with position"""


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square

        Args:
            size (int): size of the square (default 0)
            position (tuple): tuple of two positive integers (default (0,0))
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # with position offset"""
        if self.__size == 0:
            print()
            return

        # Print vertical offset (position[1])
        for _ in range(self.__position[1]):
            print()

        # Print the square lines with horizontal offset (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
