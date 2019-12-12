#!/usr/bin/python

import sys


def making_change(amount, denominations):
    cache = {}

    def making_change_inner(amount, denominations):
        key = str(amount) + str(denominations)

        nonlocal cache
        if key in cache:
            return cache[key]
        if amount == 0:
            return 1
        elif (amount < 0 or denominations == []):
            return 0
        else:
            value = making_change_inner(
                amount - denominations[-1], denominations) + making_change_inner(amount, denominations[:-1])

            if key not in cache:
                cache[key] = value

            return value

    r = making_change_inner(amount, denominations)

    return r


denominations = [1, 5, 10, 25, 50]
print(making_change(300, denominations))

if __name__ == "__main__":
        # Test our your implementation from the command line
        # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
