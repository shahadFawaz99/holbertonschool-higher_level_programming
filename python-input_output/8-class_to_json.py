#!/usr/bin/python3
"""Function that returns the dictionary description for JSON serialization."""

def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object."""
    return obj.__dict__
