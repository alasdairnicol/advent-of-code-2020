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

MONSTER = """\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""


def sort_edge(edge):
    return min(edge, edge[::-1])


def vertical_flip(tile, comment="Flipped vertically"):
    lines = tile.lines[::-1]
    return Tile(tile.number, lines, comment=comment)


def rotate_clockwise(tile, comment="Rotated 90 deg"):
    lines = ["".join(i) for i in zip(*tile.lines[::-1])]
    return Tile(tile.number, lines, comment=comment)


def orientations(original_tile):
    tile = Tile(original_tile.number, original_tile.lines, comment="original")
    yield tile
    for deg in [90, 180, 270]:
        tile = rotate_clockwise(tile, comment=f"Rotated {deg}deg")
        yield tile

    tile = vertical_flip(original_tile)
    yield tile
    for deg in [90, 180, 270]:
        tile = rotate_clockwise(
            tile, comment=f"Rotated {deg}deg and flipped vertically"
        )
        yield tile


class Tile:
    def __init__(self, number, lines, comment=""):
        self.number = number
        self.lines = lines
        self.comment = comment

    def display(self):
        print(f"Tile {self.number} {self.comment}")
        for l in self.lines:
            print("".join(l))

    @property
    def edges(self):
        return {
            "top": self.lines[0],
            "right": "".join([l[-1] for l in self.lines]),
            "bottom": self.lines[-1],
            "left": "".join([l[0] for l in self.lines]),
        }

    @property
    def sorted_edges(self):
        return {sort_edge(v) for v in self.edges.values()}


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


def find_matching_tile(remaining_tiles, matching_value, side_to_check):
    for tile in remaining_tiles.values():
        for tile in orientations(tile):
            if tile.edges[side_to_check] == matching_value:
                return tile


def main():
    tiles = load_tiles(read_input())
    sorted_edges = itertools.chain.from_iterable(t.sorted_edges for t in tiles)
    edges_count = collections.Counter(sorted_edges)
    outside_edges = {k for k, v in edges_count.items() if v == 1}
    corner_tiles = [t for t in tiles if len(set(t.sorted_edges & outside_edges)) == 2]

    jigsaw = {}
    remaining_tiles = {t.number: t for t in tiles}
    column, row = 0, 0
    tile = corner_tiles[0]
    for tile in orientations(tile):
        if (
            sort_edge(tile.edges["top"]) in outside_edges
            and sort_edge(tile.edges["left"]) in outside_edges
        ):
            break
    jigsaw[(column, row)] = tile
    del remaining_tiles[tile.number]

    while remaining_tiles:
        if sort_edge(tile.edges["bottom"]) in outside_edges:
            row = 0
            previous_tile = jigsaw[(column, 0)]
            column += 1
            matching_value = previous_tile.edges["right"]
            side_to_check = "left"
        else:
            previous_tile = jigsaw[(column, row)]
            row += 1
            matching_value = previous_tile.edges["bottom"]
            side_to_check = "top"

        tile = find_matching_tile(remaining_tiles, matching_value, side_to_check)
        jigsaw[(column, row)] = tile
        del remaining_tiles[tile.number]

    width = max(x for (x, y) in jigsaw) + 1
    height = max(y for (x, y) in jigsaw) + 1

    # print(math.prod(t.number for t in corner_tiles))

    # Stitch grid together
    lines = []
    tile_dimension = len(jigsaw[(0, 0)].lines)
    for j in range(height):
        for j2 in range(1, tile_dimension - 1):
            line = "".join(jigsaw[(i, j)].lines[j2][1:-1] for i in range(width))
            lines.append(line)

    final_tile = Tile(0, lines, comment="Final tile")

    for tile in orientations(final_tile):
        num_monsters = count_monsters(tile)
        if num_monsters:
            break

    roughness = sum(l.count("#") for l in final_tile.lines) - num_monsters * 15
    print(roughness)


def count_monsters(tile):
    count = 0
    length = len(tile.lines)
    monster_coords = [
        (i, j)
        for j, l in enumerate(MONSTER.split("\n"))
        for i, val in enumerate(l)
        if val == "#"
    ]
    for j in range(length):
        for i in range(length):
            try:
                if all(tile.lines[j + dy][i + dx] == "#" for dx, dy in monster_coords):
                    count += 1
            except IndexError:
                pass
    return count


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day20.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
