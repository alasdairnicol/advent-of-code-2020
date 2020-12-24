#!/usr/bin/env python
import itertools

TEST_INPUT = "389125467"

ACTUAL_INPUT = "219347865"

NUM_CUPS = 9


def do_turn(cups, position):
    pickup_1 = cups[position]
    pickup_2 = cups[pickup_1]
    pickup_3 = cups[pickup_2]

    destination = position
    while destination in [position, pickup_1, pickup_2, pickup_3]:
        destination -= 1
        if destination == 0:
            destination = NUM_CUPS

    cups[position] = cups[pickup_3]
    cups[pickup_3] = cups[destination]
    cups[destination] = pickup_1

    return cups[position]


def cups_to_string(cups):
    out = []
    cup = 1
    while (cup := cups[cup]) != 1:
        out.append(cup)
    return "".join(str(x) for x in out)


def main():
    num_turns = 100

    starting_cups = read_input()

    position = starting_cups[0]
    a, b = itertools.tee(starting_cups)
    next(b)
    cups = {x: y for x, y in zip(a, b)}
    cups[starting_cups[-1]] = position

    for x in range(num_turns):
        position = do_turn(cups, position)

    print(cups_to_string(cups))


def read_test_input():
    return [int(x) for x in TEST_INPUT]


def read_input():
    return [int(x) for x in ACTUAL_INPUT]


if __name__ == "__main__":
    main()
