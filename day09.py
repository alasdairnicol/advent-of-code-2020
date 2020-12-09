#!/usr/bin/env python
import itertools

TEST_INPUT = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def validate(numbers, preamble_length, position):
    preamble = set(numbers[position - preamble_length : position])
    target = numbers[position]
    for x, y in itertools.combinations(preamble, 2):
        if x + y == target:
            return True
    return False


def find_first_invalid_number(numbers, preamble_length):
    for position in range(preamble_length, len(numbers)):
        if not validate(numbers, preamble_length, position):
            return numbers[position]


def main():
    numbers = read_input()
    preamble_length = 25
    number = find_first_invalid_number(numbers, preamble_length)
    print(number)


def read_test_input():
    return [int(x) for x in TEST_INPUT.splitlines()]


def read_input():
    with open("day09.txt") as f:
        return [int(x) for x in f.read().splitlines()]


if __name__ == "__main__":
    main()
