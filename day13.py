#!/usr/bin/env python
import math

TEST_INPUT = """\
939
7,13,x,x,59,x,31,19
"""


def wait(earliest_timestamp, bus):
    return math.ceil(earliest_timestamp / bus) * bus - earliest_timestamp


def main():
    lines = read_input()
    earliest_timestamp = int(lines[0])
    buses = lines[1]
    buses = [int(b) for b in buses.split(",") if b != "x"]

    buses_and_wait = [(wait(earliest_timestamp, b), b) for b in buses]

    next_bus_id, minutes = min(buses_and_wait)
    print(next_bus_id * minutes)


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day13.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
