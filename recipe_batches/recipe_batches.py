#!/usr/bin/python

import math

"""
I need to create a function that takes in a recipe and the list of ingredients
I have on hand. It needs to compare the recipe to the ingredients as well as
their amounts set in as values. If an item is not found or a value does not
have enough ingredients for one part, return 0. Else if their is sufficient
ingredients, find how much there is of each ingredient to make a dish. return
lowest amount. 
"""


def recipe_batches(recipe, ingredients):
    # find a way to check if ingredients has enough for recipe.
    # iterate through the recipe and see if there is sufficient ingredients
    # if there is not return 0 else continue
    # take ingredients amount and dive my recipe keys

    if not (set(recipe) == set(ingredients)):
        return 0
    min = 99999999999
    for key, value in recipe.items():
        currVal = ingredients[key] // value
        if (currVal < min):
            min = currVal

    return min

# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
