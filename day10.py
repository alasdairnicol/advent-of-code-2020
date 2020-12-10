#!/usr/bin/env python
import itertools
from collections import Counter

TEST_INPUT = """\
16
10
15
5
1
11
7
19
6
12
4"""

TEST_INPUT_2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


def pairwise(iterable):
    """
    s -> (s0,s1), (s1,s2), (s2, s3), ...
    from https://docs.python.org/3/library/itertools.html
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def main():
    numbers = read_input()
    differences = Counter(y - x for x, y in pairwise(sorted(numbers)))
    # Add 1 for gap from outlet to first adapter and final adapter to device
    differences_1 = differences[1] + 1
    differences_3 = differences[3] + 1
    product = differences_1 * differences_3
    print(product)


def read_test_input():
    return [int(x) for x in TEST_INPUT.splitlines()]


def read_input():
    with open("day10.txt") as f:
        return [int(x) for x in f.read().splitlines()]


if __name__ == "__main__":
    main()
