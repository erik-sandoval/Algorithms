#!/usr/bin/python

import sys

"""
I need to take in an int and print all the possible permutations.
So if the number is two I need to loop that. Maybe a nested for loop.
"""


def rock_paper_scissors(n):
    # array to store values
    # array of rps
    rps = ['rock', 'paper', 'scissors']
    perm_arr = []

    def rps_helper():
        pass
    # for loop for first element in array.
    # print(perm_arr)
    # print(len(perm_arr))
    # print(len(perm_arr[0]))
    # for i in range(len(perm_arr)):
    #     # print(rps_index)
    #     for j in range(len(perm_arr[0])):
    #         if (rps_index == 3):
    #             rps_index = 0
    #         print(i, j, rps[rps_index])
    #         perm_arr[i][j] = rps[rps_index]
    #         rps_index += 1


rock_paper_scissors(3)

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
