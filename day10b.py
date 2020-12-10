#!/usr/bin/env python
import functools
import itertools
import math
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


def split(numbers):
    out = [0]
    previous = 0
    for x in numbers:
        if x - previous == 3:
            yield out
            out = []
        previous = x
        out.append(x)
    yield out


length_to_combinations = {
    # The values appear to be Tribonacci numbers
    # https://en.wikipedia.org/wiki/Generalizations_of_Fibonacci_numbers#Tribonacci_numbers
    1: 1,
    2: 1,
    3: 2,
    4: 4,
    5: 7,
}


@functools.cache
def num_routes(numbers, adaptor):
    """
    The number of arrangement to x is the sum of the number of
    routes to x-1, x-2 and x-3.
    """
    if adaptor == 0:
        return 1
    if adaptor not in numbers:
        return 0
    else:
        return (
            num_routes(numbers, adaptor - 1)
            + num_routes(numbers, adaptor - 2)
            + num_routes(numbers, adaptor - 3)
        )


def main():
    numbers = sorted(read_input())
    initial_approach(numbers)
    second_approach(numbers)


def initial_approach(numbers):
    """
    Split the sorted list into subsections which are 3 volts apart
    from each other.

    For each subset, the number of arrangements depends on its length.
    The answer is the product of those numbers.

    This approach solution depends on the gaps being 1 or 3 (i.e. not 2), and
    having a longest run of 5 consecutive numbers.
    """
    numbers = sorted(read_input())
    num_arrangements = math.prod(
        length_to_combinations[len(subsection)] for subsection in split(numbers)
    )
    print(num_arrangements)


def second_approach(numbers):
    """
    Solve recursively
    """
    # Turn into tuple so it's hashable by functools.cache,
    # and add the device to the end of the list
    numbers = tuple(numbers) + (numbers[-1] + 3,)
    num_arrangements = num_routes(tuple(numbers), numbers[-1])
    print(num_arrangements)


def read_test_input():
    return [int(x) for x in TEST_INPUT_2.splitlines()]


def read_input():
    with open("day10.txt") as f:
        return [int(x) for x in f.read().splitlines()]


if __name__ == "__main__":
    main()
