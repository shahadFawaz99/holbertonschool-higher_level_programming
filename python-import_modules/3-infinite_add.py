#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    addittion = 0

    for i in range(1, len(sys.argv)):
        addittion = addittion + int(sys.argv[i])

    print("{}".format(addittion))
