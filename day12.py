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

rotate_left = {
    "N": "W",
    "W": "S",
    "S": "E",
    "E": "N",
}


def rotate(direction, action, value):
    if action == "R":
        action, value = "L", 360 - value

    for x in range(value // 90):
        direction = rotate_left[direction]

    return direction


def move(x, y, direction, instruction):
    action = instruction[0]
    value = int(instruction[1:])

    if action == "F":
        action = direction

    if action == "N":
        y += value
    elif action == "S":
        y -= value
    elif action == "E":
        x += value
    elif action == "W":
        x -= value
    elif action in {"L", "R"}:
        direction = rotate(direction, action, value)
    return x, y, direction


def main():
    instructions = read_input()

    x, y, direction = 0, 0, "E"

    for instruction in instructions:
        x, y, direction = move(x, y, direction, instruction)
    manhattan_distance = abs(x) + abs(y)

    print(manhattan_distance)


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day12.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
