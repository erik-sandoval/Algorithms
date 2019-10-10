#!/usr/bin/python

import sys

"""
I need to take in an int and print all the possible permutations.
So if the number is two I need to loop that. Maybe a nested for loop.

So maybe this problem can be solved similar to how merge sort is solved.
You keep going to the end of the array until no values and you return the
solution.
"""


def rock_paper_scissors(n):
    pass


rock_paper_scissors(2)

# create a predetermined list length.
rps_arr = [[0, 0], [0, 0], [0, 0]]
rps = ['rock', 'paper', 'scissors']

rps_arr[0][0] = rps[0]

rps_arr[0][1] = rps[0]

rps_arr[1][0] = rps[0]

rps_arr[1][1] = rps[1]

rps_arr[2][0] = rps[0]

rps_arr[2][1] = rps[2]

# print(rps_arr)

# print([[0] * 2] * 3 * 3)


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_plays = int(sys.argv[1])
#         print(rock_paper_scissors(num_plays))
#     else:
#         print('Usage: rps.py [num_plays]')
