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

cache = [0 for i in range(501)]


def eating_cookies(n, cache={}):

    if (n <= 0):
        return 1

    if (n == 1):
        return 1

    if (n == 2):
        return 2

    if n in cache:
        return cache[n]

    else:
        res = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        cache[n] = res

        return cache[n]


# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         num_cookies = int(sys.argv[1])
#         print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
#             ways=eating_cookies(num_cookies), n=num_cookies))
#     else:
#         print('Usage: eating_cookies.py [num_cookies]')
