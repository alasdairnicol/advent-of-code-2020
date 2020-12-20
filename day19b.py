#!/usr/bin/env python
import re

TEST_INPUT = """\
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
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


def max_repeats(rules, messages, rule_number):
    x = 0
    rule = expand_rule(rules, rule_number)
    while True:
        regex = re.compile("%s{%s}" % (rule_to_regex(rule), x + 1))
        matching_messages = [m for m in messages if regex.search(m)]
        if not matching_messages:
            break
        x += 1
    return x


def main():
    lines = read_input()
    rules, messages = parse_input(lines)

    rule_31 = expand_rule(rules, 31)
    rule_42 = expand_rule(rules, 42)

    regex_31 = rule_to_regex(rule_31)
    regex_42 = rule_to_regex(rule_42)

    max_repeats_42 = max_repeats(rules, messages, 42)
    max_repeats_31 = max_repeats(rules, messages, 31)

    new_regex_8 = "%s{1,%s}" % (regex_42, max_repeats_42)
    new_regex_11_parts = [
        "%s{%s}%s{%s}" % (regex_42, x, regex_31, x)
        for x in range(1, max_repeats_31 + 1)
    ]
    new_regex_11 = f"({'|'.join(new_regex_11_parts)})"

    regex = new_regex_8 + new_regex_11
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
