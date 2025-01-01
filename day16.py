#!/usr/bin/env python
import itertools

TEST_INPUT = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""


def parse_range(range_string):
    """Converts a string '13-40' to a list [13,40]"""
    return [int(x) for x in range_string.split("-")]


def parse_ticket(lines):
    valid_ranges = {}
    while lines:
        line = lines.pop(0)
        if not line:
            continue
        if line == "your ticket:":
            break
        key, value = line.split(":")
        ranges = [parse_range(v) for v in value.split("or")]
        valid_ranges[key] = ranges

    your_ticket = [int(x) for x in lines.pop(0).split(",")]

    lines.pop(0)
    lines.pop(0)

    nearby_tickets = []
    while lines:
        line = [int(x) for x in lines.pop(0).split(",")]
        nearby_tickets.append(line)

    return valid_ranges, your_ticket, nearby_tickets


def validate_number(number, ranges):
    return any(number >= lower and number <= upper for lower, upper in ranges)


def main():
    lines = read_input()
    valid_ranges, your_ticket, nearby_tickets = parse_ticket(lines)
    all_ranges = sorted(itertools.chain.from_iterable(valid_ranges.values()))

    invalid_numbers = itertools.chain.from_iterable(
        [x for x in ticket if not validate_number(x, all_ranges)]
        for ticket in nearby_tickets
    )

    error_rate = sum(invalid_numbers)
    print(error_rate)


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day16.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
