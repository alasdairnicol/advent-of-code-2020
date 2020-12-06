#!/usr/bin/env python
import collections

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
    sum_questions = sum(num_questions_everyone_answered(g) for g in groups)
    print(sum_questions)


def num_questions_anyone_answered(group):
    return len(set(group) - {"\n"})


def num_questions_everyone_answered(group):
    print("group: ", group)
    counts = collections.Counter(group)
    print(counts)
    num_people = len(group.split("\n"))
    return len([k for k, v in counts.items() if v == num_people])


def read_test_input():
    return TEST_INPUT.strip().split("\n\n")


def read_input():
    with open("day06.txt") as f:
        return f.read().strip().split("\n\n")


if __name__ == "__main__":
    main()
