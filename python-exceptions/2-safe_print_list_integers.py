#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (TypeError, ValueError):
                # Skip non-integer silently
                pass
    except IndexError:
        # This is expected if x > len(my_list)
        pass
    print()
    return count
