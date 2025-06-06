#!/usr/bin/python3
"""Convert CSV data to JSON file."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file to JSON file named data.json.

    Args:
        csv_filename (str): The CSV filename to read from.

    Returns:
        bool: True if conversion successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
