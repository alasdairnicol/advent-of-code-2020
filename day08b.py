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
    original_instructions = parse_lines(lines)

    output = None

    for instructions in generate_programs(original_instructions):
        try:
            output = run_program(instructions)
        except Exception as e:
            pass
        else:
            break

    print(output)


def generate_programs(original_instructions):
    for i, [op, arg] in enumerate(original_instructions):
        instructions = original_instructions[:]

        if op == "jmp":
            instructions[i] = ("nop", arg)
        elif op == "nop":
            instructions[i] = ("jmp", arg)
        else:
            continue

        yield instructions


def run_program(instructions):
    seen = set()
    accumulator = 0
    position = 0

    while position != len(instructions):
        if position in seen:
            raise ValueError("Infinite loop detected")

        seen.add(position)
        op, arg = instructions[position]
        if op == "acc":
            accumulator += arg
            position += 1
        elif op == "jmp":
            position += arg
        elif op == "nop":
            position += 1

    return accumulator


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day08.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
