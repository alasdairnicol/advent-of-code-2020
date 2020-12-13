#!/usr/bin/env python
import math

TEST_INPUT = """\
939
7,13,x,x,59,x,31,19
"""


def main():
    buses = read_input()[1]
    buses_with_offsets = [
        (int(b), offset) for offset, b in enumerate(buses.split(",")) if b != "x"
    ]

    time = 0
    multiplier = 1
    for bus, offset in buses_with_offsets:
        while (time + offset) % bus:
            time += multiplier
        multiplier = math.lcm(multiplier, bus)

    print(time)


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day13.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
