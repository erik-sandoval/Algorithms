#!/usr/bin/python

import argparse

"""
I need to create a function that goes through each index of the array and
compares it to the previous. If it gives the max profit based off buying
and selling price, I should return that value.
"""

# O(n^2)
def find_max_profit(prices):
    # have a variable that hold that max selling point.
    max = -99999999999999999

    # use a for loop to iterate through the values
    for i in range(len(prices)):

        for j in range(i + 1, len(prices)):
            # compare each index value and see which has the highest profit margin
            if (prices[j] - prices[i] > max):
                # make that value become the highest if a new one is found.
                max = prices[j] - prices[i]
    return max


print(find_max_profit([1050, 270, 1540, 3800, 2]))

# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
