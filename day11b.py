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


class BaseGrid:
    occupied_threshold = 0

    def __init__(self, grid, width, height):
        # FIXME avoid having to pass width and height around
        self.grid = grid
        self.width = width
        self.height = height

    @classmethod
    def from_lines(cls, lines):
        grid = {}
        for j, line in enumerate(lines):
            for i, val in enumerate(line):
                grid[(i, j)] = val
        return cls(grid, i + 1, j + 1)

    def display(self):
        for j in range(self.height):
            print("".join(self.grid[(i, j)] for i in range(self.width)))

    def num_occupied(self):
        return sum(1 if val == "#" else 0 for val in self.grid.values())

    def __eq__(self, other):
        return self.grid == other.grid

    def next_grid(self):
        grid = {}
        for position in self.grid:
            grid[position] = self.get_next_value(position)

        return type(self)(grid, self.width, self.height)

    def nearby_seats_to_consider(self, position):
        return iter(())

    def num_occupied_nearby_seats(self, position):
        return sum(
            1 if self.grid[n] == "#" else 0
            for n in self.nearby_seats_to_consider(position)
        )

    def get_next_value(self, position):
        value = self.grid[position]  # By default value doesn't change
        if value == "L" and self.num_occupied_nearby_seats(position) == 0:
            value = "#"
        elif (
            value == "#"
            and self.num_occupied_nearby_seats(position) >= self.occupied_threshold
        ):
            value = "L"
        return value


class NearestNeighbourGrid(BaseGrid):
    occupied_threshold = 4

    def nearby_seats_to_consider(self, position):
        deltas = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for dx, dy in deltas:
            neighbour = (position[0] + dx, position[1] + dy)
            if neighbour in self.grid:
                yield neighbour


class FirstVisibleSeatGrid(BaseGrid):
    occupied_threshold = 5

    def nearby_seats_to_consider(self, position):
        deltas = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for dx, dy in deltas:
            x, y = position[0] + dx, position[1] + dy
            while True:
                val = self.grid.get((x, y))
                if val in {"#", "L"}:
                    # We have found a seat
                    yield (x, y)
                    break
                elif val == None:
                    # We have reached the end of the grid
                    break
                else:
                    # continue looking
                    x, y = x + dx, y + dy


def main():
    lines = read_input()
    grid = FirstVisibleSeatGrid.from_lines(lines)
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
