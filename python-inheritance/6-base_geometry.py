#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Base class for geometry-related operations."""

    def area(self):
        """Raises an Exception indicating that area is not implemented."""
        raise Exception("area() is not implemented")
