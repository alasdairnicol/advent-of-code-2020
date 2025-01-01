#!/usr/bin/env python

TEST_INPUT = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


def gen_bag_dict(lines):
    return dict(parse_line(l) for l in lines)


def contains_colour(bag_dict, holder, colour):
    contents = bag_dict[holder]
    for num, bag in contents:
        if bag == colour:
            return True
        if contains_colour(bag_dict, bag, colour):
            return True
    return False


def num_bags_contain_colour(bag_dict, colour):
    return len([k for k in bag_dict if contains_colour(bag_dict, k, colour)])


def main():
    bag_dict = gen_bag_dict(read_input())
    shiny_gold = "shiny gold"
    count = num_bags_contain_colour(bag_dict, shiny_gold)
    print(f"Part A: {count}")


def split_content(content):
    if content.strip() == "no other":
        return None
    num, colour = content.strip().split(" ", maxsplit=1)
    return (int(num), colour)


def parse_line(line):
    line = line.rstrip(".").replace("bags", "").replace("bag", "")
    holder, contents = line.split("contain")
    holder = holder.strip()
    contents = [x for c in contents.split(",") if (x := split_content(c))]
    return holder, contents


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day07.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
