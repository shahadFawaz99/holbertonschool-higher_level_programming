#!/usr/bin/python3
"""erialize and deserialize custom Python objects using the pickle"""
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\n\
              Is Student: {self.is_student}".format())

    def serialize(self, filename):
        """serialize the object and save it to file"""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    def deserialize(filename):
        """deserialize data from file and return"""
        try:
            with open(filename, "rb") as file:
                self = pickle.load(file)
        except Exception as e:
            return None
        return self
