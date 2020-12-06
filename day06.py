#!/usr/bin/env python

TEST_INPUT = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def main():
    groups = read_input()
    sum_questions = sum(num_questions_anyone_answered(g) for g in groups)
    print(sum_questions)


def num_questions_anyone_answered(group):
    return len(set(group) - {"\n"})


def read_test_input():
    return TEST_INPUT.split("\n\n")


def read_input():
    with open("day06.txt") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()
