#!/usr/bin/env python
import itertools
from collections import Counter

TEST_INPUT = """\
F10
N3
F7
R90
F11
"""


def rotate(waypoint, action, value):
    if action == "L":
        action, value = "R", 360 - value

    if value == 90:
        waypoint = (waypoint[1], -waypoint[0])
    elif value == 180:
        waypoint = (-waypoint[0], -waypoint[1])
    elif value == 270:
        waypoint = (-waypoint[1], waypoint[0])

    return waypoint


def move(waypoint, ship, instruction):
    action = instruction[0]
    value = int(instruction[1:])

    if action == "F":
        ship = (ship[0] + waypoint[0] * value, ship[1] + waypoint[1] * value)
    elif action == "N":
        waypoint = (waypoint[0], waypoint[1] + value)
    elif action == "S":
        waypoint = (waypoint[0], waypoint[1] - value)
    elif action == "E":
        waypoint = (waypoint[0] + value, waypoint[1])
    elif action == "W":
        waypoint = (waypoint[0] - value, waypoint[1])
    elif action in {"L", "R"}:
        waypoint = rotate(waypoint, action, value)

    return waypoint, ship


def main():
    instructions = read_input()

    waypoint = (10, 1)
    ship = (0, 0)

    for instruction in instructions:
        waypoint, ship = move(waypoint, ship, instruction)
    manhattan_distance = abs(ship[0]) + abs(ship[1])

    print(manhattan_distance)


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day12.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
