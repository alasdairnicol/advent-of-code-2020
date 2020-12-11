#!/usr/bin/env python
import itertools
from collections import Counter

TEST_INPUT = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


class Grid:
    def __init__(self, grid, width, height):
        # FIXME avoid having to pass width and height around
        self.grid = grid
        self.width = width
        self.height = height

    @staticmethod
    def from_lines(lines):
        grid = {}
        for j, line in enumerate(lines):
            for i, val in enumerate(line):
                grid[(i, j)] = val
        return Grid(grid, i + 1, j + 1)

    def neighbours(self, position):
        deltas = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for dx, dy in deltas:
            neighbour = (position[0] + dx, position[1] + dy)
            if neighbour in self.grid:
                yield neighbour

    def num_occupied_neighbours(self, position):
        return sum(1 if self.grid[n] == "#" else 0 for n in self.neighbours(position))

    def display(self):
        for j in range(self.height):
            print("".join(self.grid[(i, j)] for i in range(self.width)))

    def next_grid(self):
        grid = {}
        for (x, y), value in self.grid.items():
            next_value = value  # assume it doesn't change
            if value == "L" and self.num_occupied_neighbours((x, y)) == 0:
                next_value = "#"
            elif value == "#" and self.num_occupied_neighbours((x, y)) >= 4:
                next_value = "L"

            grid[(x, y)] = next_value

        return Grid(grid, self.width, self.height)

    def num_occupied(self):
        return sum(1 if val == "#" else 0 for val in self.grid.values())

    def __eq__(self, other):
        return self.grid == other.grid


def main():
    lines = read_input()
    grid = Grid.from_lines(lines)
    while True:
        old_grid = grid
        grid = old_grid.next_grid()
        if grid == old_grid:
            break

    print(grid.num_occupied())


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day11.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
