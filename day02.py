#!/usr/bin/env python
import re

regex = re.compile(
    r"^(?P<lowest>\d+)-(?P<highest>\d+) (?P<letter>[a-z]): (?P<password>[a-z]+)$"
)


def main():
    count = sum(validate_line(line) for line in read_input())
    print(count)


def validate_line(line):
    lowest, highest, letter, password = regex.match(line).groups()
    count = password.count(letter)
    lowest = int(lowest)
    highest = int(highest)
    return lowest <= count <= highest


def read_input():
    with open("day02.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
