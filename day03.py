#!/usr/bin/env python


class Grid:
    def __init__(self, grid_input):
        self.grid = {}
        for j, line in enumerate(grid_input):
            for i, val in enumerate(line):
                self.grid[(i, j)] = val == "#"
        self.height = j + 1
        self.width = i + 1

    def get_value(self, i, j):
        return self.grid[(i % self.width, j)]


TEST_INPUT = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def count_trees_for_slope(grid, right, down):
    trees = 0
    i, j = 0, 0
    while j < grid.height:
        if grid.get_value(i, j):
            trees += 1
        j += down
        i += right
    return trees


def main():
    grid = Grid(read_input())
    print(count_trees_for_slope(grid, 3, 1))


def read_input():
    """Return list of strings for each line with \n stripped"""
    with open("day03.txt") as f:
        return (l.strip() for l in f.readlines())


def read_test_input():
    """Return list of strings for each line with \n stripped"""
    return TEST_INPUT.split("\n")


if __name__ == "__main__":
    main()
