#!/usr/bin/env python
import itertools


def main():
    entries = list(read_input())
    x, y = find_entries(entries)
    product = x * y
    print(product)


def find_entries(entries, target=2020):
    for x, y in itertools.combinations(entries, 2):
        if x + y == target:
            return x, y


def read_input():
    with open("day01.txt") as f:
        return (int(x) for x in f.readlines())


if __name__ == "__main__":
    main()
