#!/usr/bin/python3
"""
This module contains one function: add_integer(a, b=98)
It adds two integers and returns the result.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers).
    Args:
        a: first number (int or float)
        b: second number (int or float), default is 98
    Returns:
        The sum of a and b casted to integers
    Raises:
        TypeError: if a or b is not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
