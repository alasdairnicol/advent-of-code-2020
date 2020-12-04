#!/usr/bin/env python
import re

TEST_INPUT = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

REQUIRED_FIELDS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid", # Omit cid from required fields
}


def main():
    passports = process_batch(read_input())
    num_valid = len([p for p in passports if validate_passport(p)])
    print(num_valid)


def validate_passport(passport):
    missing_fields = REQUIRED_FIELDS - passport.keys()
    if missing_fields:
        return False

    try:
        byr = int(passport["byr"])
    except ValueError:
        return False
    else:
        if byr < 1920 or byr > 2002:
            return False

    try:
        iyr = int(passport["iyr"])
    except ValueError:
        return False
    else:
        if iyr < 2010 or iyr > 2020:
            return False

    try:
        eyr = int(passport["eyr"])
    except ValueError:
        return False
    else:
        if eyr < 2020 or eyr > 2030:
            return False

    hgt = passport["hgt"]
    if hgt.endswith("cm"):
        try:
            hgt = int(hgt[:-2])
        except ValueError:
            return False
        else:
            if hgt < 150 or hgt > 193:
                return False
    elif hgt.endswith("in"):
        try:
            hgt = int(hgt[:-2])
        except ValueError:
            return False
        else:
            if hgt < 59 or hgt > 76:
                return False
    else:
        return False

    if not re.match(r"^#[0-9a-f]{6}$", passport["hcl"]):
        return False

    if passport["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False

    if not re.match(r"^[0-9]{9}$", passport["pid"]):
        return False

    return True


def process_batch(input_lines):
    passports = []
    passport = {}
    for line in input_lines:
        if line.strip():
            for part in line.split():
                key, value = part.split(":")
                passport[key] = value
        else:
            if passport:
                passports.append(passport)
            passport = {}
    if passport:
        passports.append(passport)
    return passports


def read_input():
    """Return list of strings for each line with \n stripped"""
    with open("day04.txt") as f:
        return f.readlines()


def read_test_input():
    """Return list of strings for each line with \n stripped"""
    return TEST_INPUT.split("\n")


if __name__ == "__main__":
    main()
