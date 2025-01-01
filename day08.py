#!/usr/bin/env python

TEST_INPUT = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def parse_line(line):
    operation, argument = line.split()
    argument = int(argument)
    return operation, argument


def parse_lines(lines):
    return [parse_line(l) for l in lines]


def main():
    lines = read_input()
    instructions = parse_lines(lines)

    seen = set()
    accumulator = 0
    position = 0

    while position not in seen:
        seen.add(position)
        op, arg = instructions[position]
        if op == "acc":
            accumulator += arg
            position += 1
        elif op == "jmp":
            position += arg
        elif op == "nop":
            position += 1

    print(accumulator)


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day08.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
