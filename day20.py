#!/usr/bin/env python
import re
import collections
import itertools
import math

TEST_INPUT = """\
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
"""


class Tile:
    def __init__(self, number, lines):
        self.number = number
        self.lines = lines

    def display(self):
        print(f"Tile {self.number}")
        for l in self.lines:
            print("".join(l))

    def edges(self):
        edges = [
            self.lines[0],
            "".join([l[-1] for l in self.lines]),
            self.lines[-1],
            "".join([l[0] for l in self.lines]),
        ]
        sorted_edges = [min(e, e[::-1]) for e in edges]
        return sorted_edges


def load_tiles(lines):
    tiles = []
    while lines:
        line = lines.pop(0)
        number = int(line.split()[1].rstrip(":"))
        tile_lines = []
        while lines and (line := lines.pop(0)):
            tile_lines.append(line)
        tile = Tile(number, tile_lines)
        tiles.append(tile)
    return tiles


def main():
    tiles = load_tiles(read_input())
    edges = itertools.chain.from_iterable(t.edges() for t in tiles)
    edges_count = collections.Counter(edges)
    outside_edges = {k for k, v in edges_count.items() if v == 1}
    corner_tiles = [t for t in tiles if len(set(t.edges()) & outside_edges) == 2]
    print(math.prod([t.number for t in corner_tiles]))


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day20.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
