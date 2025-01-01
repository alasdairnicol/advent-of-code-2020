#!/usr/bin/env python
import re
import functools
import itertools

TEST_INPUT = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

regex = re.compile(r"([\w ]+) \(contains ([\w, ]+)\)")


def main():
    foods = read_input()
    ingredients_allergens = []
    for food in foods:
        ingredients, allergens = regex.match(food).groups()
        ingredients = {i.strip() for i in ingredients.split()}
        allergens = {a.strip() for a in allergens.split(",")}
        ingredients_allergens.append([ingredients, allergens])

    all_ingredients = set(
        itertools.chain.from_iterable(i for i, _ in ingredients_allergens)
    )
    all_allergens = set(
        itertools.chain.from_iterable(a for _, a in ingredients_allergens)
    )

    # Map food to possible allergens
    allergens_dict = {}
    for a in all_allergens:
        allergens_dict[a] = set.intersection(
            *(
                ingredients
                for ingredients, allergens in ingredients_allergens
                if a in allergens
            )
        )

    # Map food to a single allergen
    actual_allergens = {}
    while allergens_dict:
        for food, allergens in list(allergens_dict.items()):
            if len(allergens) == 1:
                allergen = allergens.pop()
                actual_allergens[allergen] = food
                del allergens_dict[food]
                for v in allergens_dict.values():
                    v.discard(allergen)

    sorted_allergens = sorted(actual_allergens, key=lambda k: actual_allergens[k])
    print(",".join(sorted_allergens))


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day21.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
