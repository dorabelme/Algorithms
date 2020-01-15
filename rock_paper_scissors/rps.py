#!/usr/bin/python

import sys
from itertools import product


# def rock_paper_scissors(n):
#     rpc = ['rock', 'paper', 'scissors']
#     if n == 1:
#         return [['rock'], ['paper'], ['scissors']]
#     else:
#         return [list(x) for x in list(product(rpc, repeat=n))]


def rock_paper_scissors(n):
    elements = ['rock', 'paper', 'scissors']
    elements_array = [[e] for e in elements]

    if n == 1:
        return elements_array
    if n <= 0:
        return [[]]
    else:
        first_row = []

        for i in elements:
            e = [i] * (3 ** (n - 1))
            for _e in e:
                first_row.append([_e])

        rest_rows = rock_paper_scissors(n - 1) * 3

        result = [first_array + second_array for first_array,
                  second_array in zip(first_row, rest_rows)]

        print("Number of combinations: %d" % len(result))

        return result


# print(rock_paper_scissors(2))
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
