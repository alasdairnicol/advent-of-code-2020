#!/usr/bin/env python
import functools
import math

TEST_INPUT = """\
939
7,13,x,x,59,x,31,19
"""


def get_time_and_multiplier(acc, new_bus_info):
    multiplier, time = acc
    bus, offset = new_bus_info
    while (time + offset) % bus:
        time += multiplier
    multiplier = math.lcm(multiplier, bus)
    return multiplier, time


def main():
    buses = read_input()[1]
    buses_with_offsets = [
        (int(b), offset) for offset, b in enumerate(buses.split(",")) if b != "x"
    ]
    # We get the same answer without the (1, 0) initialiser, but I believe that
    # it is required to handle the case where the first offset is not zero
    _, time = functools.reduce(get_time_and_multiplier, buses_with_offsets, (1, 0))

    print(time)


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day13.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
