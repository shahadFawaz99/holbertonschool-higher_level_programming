#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as c

    a = 10
    b = 5

    print("{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}".format(
        a, b, c.add(a, b),
        a, b, c.sub(a, b),
        a, b, c.mul(a, b),
        a, b, c.div(a, b)
    ))
