#!/usr/bin/env python


def get_seat_id(boarding_pass):
    # Original approach was to calculate row and column separately
    # No need to do this because seat_id = 8 * row + column
    # row, column = boarding_pass[:7], boarding_pass[7:]

    # row = "".join("0" if x == "F" else "1" for x in row)
    # row_num = int(row, 2)

    # column = "".join("0" if x == "L" else "1" for x in column)
    # column_num = int(column, 2)

    # return 8*row_num + column_num

    return int("".join("0" if x in {"F", "L"} else "1" for x in boarding_pass), 2)


def get_missing_id(seat_ids):
    for x in range(min(seat_ids) + 1, max(seat_ids)):
        if x not in seat_ids:
            return x


def main():
    seat_ids = set(get_seat_id(boarding_pass.strip()) for boarding_pass in read_input())
    missing_seat = get_missing_id(seat_ids)
    print(missing_seat)


def read_input():
    with open("day05.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
