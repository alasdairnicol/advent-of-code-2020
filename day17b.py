#!/usr/bin/env python
from collections import Counter
import itertools
import math

TEST_INPUT = """\
.#.
..#
###
"""

NUM_BOOT_CYLES = 6


class Grid:
    def __init__(self, grid):
        # FIXME avoid having to pass width and height around
        self.grid = grid

        self.min_x = min(k[0] for k in self.grid)
        self.min_y = min(k[1] for k in self.grid)
        self.min_z = min(k[2] for k in self.grid)
        self.min_w = min(k[3] for k in self.grid)
        self.max_x = max(k[0] for k in self.grid)
        self.max_y = max(k[1] for k in self.grid)
        self.max_z = max(k[2] for k in self.grid)
        self.max_w = max(k[3] for k in self.grid)
        self.width = len(set(k[0] for k in self.grid))
        self.height = len(set(k[1] for k in self.grid))
        self.depth = len(set(k[2] for k in self.grid))
        self.w_length = len(set(k[3] for k in self.grid))

    @classmethod
    def from_lines(cls, lines):
        grid = {}
        k = 0
        l = 0
        for j, line in enumerate(lines):
            for i, val in enumerate(line):
                grid[(i, j, k, l)] = val
        return cls(grid)

    def display(self):
        for l in range(self.min_w, self.max_w + 1):
            for k in range(self.min_z, self.max_z + 1):
                print(f"z={k}, w={l}")
                for j in range(self.min_y, self.max_y + 1):
                    print(
                        "".join(
                            self.grid[(i, j, k, l)]
                            for i in range(self.min_x, self.max_x + 1)
                        )
                    )
                print()

    def count(self, position):
        if self.grid.get(position) == "#":
            val = 1
            if position[2] != 0:
                val *= 2
            if position[3] != 0:
                val *= 2
        else:
            val = 0
        return val

    def num_active(self):
        return sum(self.count(position) for position in self.grid)

    def __eq__(self, other):
        return self.grid == other.grid

    def next_grid(self):
        grid = {}
        for w in range(self.min_w, self.max_w + 2):
            for z in range(self.min_z, self.max_z + 2):
                for y in range(self.min_y - 1, self.max_y + 2):
                    for x in range(self.min_x - 1, self.max_x + 2):
                        grid[(x, y, z, w)] = self.get_next_value((x, y, z, w))

        return Grid(grid)

    def get_next_value(self, position):
        active_neighbours = sum(
            1 if self.get_value(n) == "#" else 0 for n in get_neighbours(position)
        )
        val = self.get_value(position)
        if val == "#":
            if active_neighbours in (2, 3):
                next_val = "#"
            else:
                next_val = "."
        else:
            if active_neighbours == 3:
                next_val = "#"
            else:
                next_val = "."
        return next_val

    def get_value(self, position):
        x, y, z, w = position
        w = abs(w)
        z = abs(z)
        return self.grid.get((x, y, z, w), ".")


def get_neighbours(position):
    x, y, z, w = position
    return (
        (x + dx, y + dy, z + dz, w + dw)
        for dx, dy, dz, dw in itertools.product((-1, 0, 1), repeat=4)
        if (dx, dy, dz, dw) != (0, 0, 0, 0)
    )


def main():
    lines = read_input()
    grid = Grid.from_lines(lines)
    # grid.display()

    for cycle in range(NUM_BOOT_CYLES):
        grid = grid.next_grid()
        # grid.display()

    print(grid.num_active())


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day17.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
