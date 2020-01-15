#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    total_batches = None

    for key in recipe.keys():
        # Check if the key exists in ingredients
        if key not in ingredients:
            return 0

        # Calculate if batch in ingredients is enough
        batches = ingredients[key] // recipe[key]
        if batches == 0:
            return 0

        if total_batches:
            total_batches = min(total_batches, batches)
        else:
            total_batches = batches

    return total_batches


recipe = {'milk': 100, 'butter': 50, 'cheese': 10}
ingredients = {
    'milk': 198, 'butter': 52, 'cheese': 10}
print(recipe_batches(recipe, ingredients))

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
