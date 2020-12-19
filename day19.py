#!/usr/bin/env python
import re

TEST_INPUT = """\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""


def tidy_part(part):
    part = part.strip('"')
    try:
        part = int(part)
    except ValueError:
        pass
    return part


def parse_input(lines):
    rules = {}

    while lines:
        line = lines.pop(0)
        if not line:
            break

        key, value = line.split(":")
        key = int(key)
        rules[key] = [tidy_part(x) for x in value.split()]

    messages = lines

    return rules, messages


def expand_rule(rules, rule):
    if rule in rules:
        return [expand_rule(rules, x) for x in rules[rule]]
    return rule


def rule_to_regex(rule):
    if len(rule) == 1 and isinstance(rule, str):
        return rule[0]
    else:
        return f'({"".join(rule_to_regex(x) for x in rule)})'


def main():
    lines = read_input()
    rules, messages = parse_input(lines)
    rule_zero = expand_rule(rules, 0)
    regex = rule_to_regex(rule_zero)
    anchored_regex = re.compile(f"^{regex}$")

    matching_messages = [m for m in messages if anchored_regex.match(m)]
    print(len(matching_messages))


def read_test_input():
    return TEST_INPUT.splitlines()


def read_input():
    with open("day19.txt") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
