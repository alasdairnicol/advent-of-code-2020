#!/usr/bin/env python

SUBJECT_NUMBER = 7

def main():
    card_public_key, door_public_key = read_input()

    card_loop_size = 0
    number = 1

    while number != card_public_key:
        number = number * SUBJECT_NUMBER % 20201227
        card_loop_size += 1

    door_encryption_key = 1
    for x in range(card_loop_size):
        door_encryption_key = door_encryption_key * door_public_key % 20201227

    print(door_encryption_key)

def read_test_input():
    return [5764801, 17807724]


def read_input():
    with open('day25.txt') as f:
        return [int(x) for x in f.read().splitlines()]


if __name__ == "__main__":
    main()
