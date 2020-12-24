#!/usr/bin/env python
import collections

TEST_INPUT = """\
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"""

moves = {
    "ne": (1, 1),
    "e": (2, 0),
    "se": (1, -1),
    "sw": (-1, -1),
    "w": (-2, 0),
    "nw": (-1, 1),
}


def locate_tile(directions):
    previous = ""
    x, y = 0, 0
    for d in directions:
        if d in "ns":
            previous = d
            continue

        d = previous + d
        previous = ""
        dx, dy = moves[d]
        x += dx
        y += dy
    return x, y


def initialise_floor(lines):
    black_tiles = set()
    for directions in lines:
        tile = locate_tile(directions)
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)
    return black_tiles


def neigbours(tile):
    x, y = tile
    for dx, dy in moves.values():
        yield x + dx, y + dy


def do_turn(black_tiles):
    neighbour_count = collections.Counter(
        neighbour for tile in black_tiles for neighbour in neigbours(tile)
    )

    black_tiles = {
        t
        for t, count in neighbour_count.items()
        if (t in black_tiles and count == 1) or count == 2
    }
    return black_tiles


def main():
    lines = read_input()
    num_turns = 100

    black_tiles = initialise_floor(lines)

    for turn in range(1, num_turns + 1):
        black_tiles = do_turn(black_tiles)
        # print(f'Day {turn}: {len(black_tiles)}')

    print(f"Day {turn}: {len(black_tiles)}")


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day24.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
