#!/usr/bin/env python
from collections import deque

TEST_INPUT = """\
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""


def read_players(lines):
    player_2_start = lines.index("Player 2:")
    xs = deque(int(x) for x in lines[1 : player_2_start - 1])
    ys = deque(int(x) for x in lines[player_2_start + 1 :])
    return xs, ys


def play_turn(xs, ys):
    x = xs.popleft()
    y = ys.popleft()
    if x > y:
        xs.extend([x, y])
    elif y > x:
        ys.extend([y, x])
    else:
        raise ValueError("Cards are equal")


def score_deck(xs):
    return sum(i * x for i, x in enumerate(reversed(xs), 1))


def main():
    lines = read_input()
    xs, ys = read_players(lines)

    while xs and ys:
        play_turn(xs, ys)

    winning_deck = xs or ys
    print(score_deck(winning_deck))


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day22.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
