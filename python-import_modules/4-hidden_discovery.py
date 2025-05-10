#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    def_names = dir(hidden_4)

    def_names.sort()

    for name in def_names:
        if not name.startswith('__'):
            print(name)

