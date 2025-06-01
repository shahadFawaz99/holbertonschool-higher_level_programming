#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size):
        """Initialize square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
