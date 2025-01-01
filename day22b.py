#!/usr/bin/env python

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

TEST_INPUT_2 = """\
Player 1:
43
19

Player 2:
2
29
14
"""


def read_players(lines):
    player_2_start = lines.index("Player 2:")
    xs = tuple(int(x) for x in lines[1 : player_2_start - 1])
    ys = tuple(int(x) for x in lines[player_2_start + 1 :])
    return xs, ys


def play_game(xs, ys):
    round = 0
    games = set()

    while xs and ys:
        game_hash = (xs, ys)
        if game_hash in games:
            return "x", xs
        else:
            games.add(game_hash)

        x, xs = xs[0], xs[1:]
        y, ys = ys[0], ys[1:]

        if len(xs) >= x and len(ys) >= y:
            winner, _ = play_game(xs[:x], ys[:y])
        elif x > y:
            winner = "x"
        elif y > x:
            winner = "y"
        else:
            raise ValueError("Cards are equal")

        if winner == "x":
            xs += (x, y)
        else:
            ys += (y, x)

    if xs:
        return "x", xs
    else:
        return "y", ys


def score_deck(xs):
    return sum(i * x for i, x in enumerate(reversed(xs), 1))


def main():
    lines = read_input()
    xs, ys = read_players(lines)

    _, winning_deck = play_game(xs, ys)
    print(score_deck(winning_deck))


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day22.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
