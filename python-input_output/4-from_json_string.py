#!/usr/bin/python3
"""
Function that returns a Python object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string into a Python object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python data structure.
    """
    return json.loads(my_str)
