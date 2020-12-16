#!/usr/bin/env python
import itertools
import math

TEST_INPUT = """\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
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


def validate_ticket(ticket, ranges):
    return all(validate_number(number, ranges) for number in ticket)


def possible_fields(values, valid_ranges):
    return {k for k, v in valid_ranges.items() if validate_ticket(values, v)}


def main():
    lines = read_input()
    valid_ranges, your_ticket, nearby_tickets = parse_ticket(lines)
    all_ranges = sorted(itertools.chain.from_iterable(valid_ranges.values()))

    valid_tickets = [t for t in nearby_tickets if validate_ticket(t, all_ranges)]

    fields_dict = {i: x for i, x in enumerate(zip(*valid_tickets))}

    # Map of position to set of possible field names
    possible_fields_dict = {
        k: possible_fields(v, valid_ranges) for k, v in fields_dict.items()
    }

    # Map of field name to position
    field_name_position = {}

    while possible_fields_dict:
        for k, v in list(possible_fields_dict.items()):
            if len(v) == 1:
                field = v.pop()
                field_name_position[field] = k
                del possible_fields_dict[k]
                for v2 in possible_fields_dict.values():
                    v2.discard(field)

    departure_keys = [k for k in valid_ranges if k.startswith("departure")]
    departure_values = [your_ticket[field_name_position[x]] for x in departure_keys]

    print(math.prod(departure_values))


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day16.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
