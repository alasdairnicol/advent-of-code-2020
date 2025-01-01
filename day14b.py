#!/usr/bin/env python
import functools
import itertools
import math
import operator
import re

TEST_INPUT = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

LINE_RE = re.compile(r"mem\[(\d+)\] = (\d+)")


def apply_mask(mask, value):
    # Set 1s to 1s
    or_mask = int(mask.replace("X", "0"), 2)
    value = value | or_mask

    # Set Xs to 0s
    and_mask = int(mask.replace("0", "1").replace("X", "0"), 2)
    value = value & and_mask

    return value


def floating_numbers(mask):
    floating = int(mask.replace("1", "0").replace("X", "1"), 2)
    values = []
    x = 1
    while floating:
        if floating & 1:
            values.append(x)
        x <<= 1
        floating >>= 1
    return [
        functools.reduce(operator.or_, p)
        for p in itertools.product(*((val, 0) for val in values))
    ]


def main():
    mem = {}

    lines = read_input()
    for line in lines:
        if line.startswith("mask ="):
            mask = line.split("=")[1].strip()
        else:
            location, value = LINE_RE.match(line).groups()
            value = int(value)
            location = apply_mask(mask, int(location))

            for floating_number in floating_numbers(mask):
                mem[location | floating_number] = value
    memory_sum = sum(mem.values())
    print(memory_sum)


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day14.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
