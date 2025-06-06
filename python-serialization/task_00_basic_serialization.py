#!/usr/bin/python3
"""Basic serialization module using JSON"""

import json


def serialize_and_save_to_file(data, filename):
    """Serializes a dictionary and saves it to a JSON file.

    Args:
        data (dict): The data to serialize.
        filename (str): The file where data will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads JSON data from a file and deserializes it to a dictionary.

    Args:
        filename (str): The file to read from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
