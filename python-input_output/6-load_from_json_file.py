#!/usr/bin/python3
"""
Function that creates a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        The Python object resulting from the deserialization of the JSON file content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
