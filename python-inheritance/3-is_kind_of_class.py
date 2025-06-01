#!/usr/bin/python3
"""Check if an object is an instance of, or inherited from, a class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of or inherited from a_class."""
    return isinstance(obj, a_class)
