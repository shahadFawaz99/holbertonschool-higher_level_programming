#!/usr/bin/python3
"""A class that inhernts another a list from nother class"""


class MyList(list):
    """ Mylist class inhernts from a built in class called list in python"""
    def print_sorted(self):
        print(sorted(self))
