#!/usr/bin/env python
from collections import Counter
import operator
import math

TEST_INPUT = """\
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
"""


def eval_line(line):
    char_list = [x for x in line if x != " "]
    return eval_char_list(char_list)


def eval_char_list(char_list):
    parts = []
    while char_list:
        char = char_list.pop(0)
        if char == "(":
            sub_list = ["("]
            paren_count = 1
            while paren_count:
                char = char_list.pop(0)
                if char == "(":
                    paren_count += 1
                elif char == ")":
                    paren_count -= 1
                sub_list.append(char)
            parts.append(eval_char_list(sub_list[1:-1]))
        else:
            parts.append(char)

    total = 0
    op = operator.add

    for part in parts:
        if part == "+":
            op = operator.add
        elif part == "*":
            op = operator.mul
        else:
            total = op(total, int(part))
    return total


def main():
    lines = read_input()

    total = sum(eval_line(l) for l in lines)
    print(total)


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day18.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
