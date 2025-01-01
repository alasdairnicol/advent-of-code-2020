#!/usr/bin/env python
import itertools
import math


def main():
    entries = list(read_input())
    subset = find_entries(entries, 2020, 3)
    product = math.prod(subset)
    print(product)


def find_entries(entries, target, num_entries):
    for subset in itertools.combinations(entries, num_entries):
        if sum(subset) == target:
            return subset


def read_input():
    with open("day01.txt") as f:
        return (int(x) for x in f.readlines())


if __name__ == "__main__":
    main()
