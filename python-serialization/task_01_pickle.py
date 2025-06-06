#!/usr/bin/python3
"""Module to pickle and unpickle a custom class."""

import pickle


class CustomObject:
    """Custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to a file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            pass  # You can optionally log or print the error

    @classmethod
    def deserialize(cls, filename):
        """Deserialize the object from a file."""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except (OSError, pickle.PickleError):
            pass
        return None
