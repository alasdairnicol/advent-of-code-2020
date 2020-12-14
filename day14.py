#!/usr/bin/env python
import math
import re

TEST_INPUT = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

LINE_RE = re.compile(r"mem\[(\d+)\] = (\d+)")


def apply_mask(mask, value):
    and_mask = int(mask.replace("X", "1"), 2)
    value = value & and_mask
    or_mask = int(mask.replace("X", "0"), 2)
    value = value | or_mask
    return value


def main():
    mem = {}

    lines = read_input()
    for line in lines:
        if line.startswith("mask ="):
            mask = line.split("=")[1].strip()
        else:
            location, value = LINE_RE.match(line).groups()
            value = int(value)
            mem[location] = apply_mask(mask, value)

    memory_sum = sum(mem.values())
    print(memory_sum)


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day14.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
