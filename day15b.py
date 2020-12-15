#!/usr/bin/env python
import math
import re

TEST_INPUT = "0,3,6"

REAL_INPUT = "1,20,8,12,0,14"

NUM_TURNS = 30000000

def main():
    starting_numbers = [int(x) for x in REAL_INPUT.split(",")]

    numbers = {}
    for turn, number in enumerate(starting_numbers, 1):
        previously_spoken = numbers.get(number, 0)
        numbers[number] = turn

    while turn < NUM_TURNS:
        if previously_spoken == 0:
            number = 0
        else:
            number = turn - previously_spoken
        turn += 1
        previously_spoken = numbers.get(number, 0)
        numbers[number] = turn

    print(number)


if __name__ == "__main__":
    main()
