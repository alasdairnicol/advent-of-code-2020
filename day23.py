#!/usr/bin/env python
import itertools

TEST_INPUT = "389125467"

ACTUAL_INPUT = "219347865"


def do_turn(cups):
    cups_loop = itertools.cycle(cups)
    current_cup = next(cups_loop)  # current cup
    picked_up = [next(cups_loop), next(cups_loop), next(cups_loop)]
    out = []
    destination = current_cup
    while destination in [current_cup] + picked_up:
        destination -= 1
        if destination == 0:
            destination = 9
    while len(out) < 9:
        next_cup = next(cups_loop)
        out.append(next_cup)
        if next_cup == destination:
            out.extend(picked_up)

    return out


def final_list_to_string(cups):
    index = cups.index(1)
    cups = (cups + cups)[index + 1 : index + 9]
    return "".join(str(x) for x in cups)


def main():
    num_turns = 100
    cups = read_input()

    for x in range(num_turns):
        cups = do_turn(cups)

    print(final_list_to_string(cups))


def read_test_input():
    return [int(x) for x in TEST_INPUT]


def read_input():
    return [int(x) for x in ACTUAL_INPUT]


if __name__ == "__main__":
    main()
