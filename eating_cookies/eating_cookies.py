#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

"""
I have to create a function that takes in a num and show how many different
ways the cookies can be eaten. with the highest being an increment of three.
he can eat 1 cookie 1 way, 2 cookies 2 ways, and 3 cookies 4 ways.
"""

counter = 0


def eating_cookies(n, cache=None):
    # keep count of how many ways there is for him to eat x amount of cookies
    # possible recursion, set up a basecase
    global counter
    if (n < 0):
        return

    if (n == 0):
        return 1

    if (n == 1):
        print('1 hit')
        counter += 1

    if (n == 2):
        print('2 hit')
        counter += 1

    if (n == 3):
        print('3 hit')
        counter += 1

    eating_cookies(n-1)
    eating_cookies(n-2)
    eating_cookies(n-3)

    return counter


print(eating_cookies(2))

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
#             ways=eating_cookies(num_cookies), n=num_cookies))
#     else:
#         print('Usage: eating_cookies.py [num_cookies]')
