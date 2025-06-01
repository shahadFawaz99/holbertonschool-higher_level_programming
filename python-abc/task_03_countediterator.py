#!/usr/bin/python3
"""CountedIterator - keeps track of number of items iterated."""


class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)  # raises StopIteration if done
        self.count += 1
        return item

    def get_count(self):
        return self.count
