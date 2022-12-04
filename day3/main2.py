# aoc2022 day3

from os import read


def read_file(filename='input.txt'):
    with open(filename, 'r') as f:
        for line in f: yield line

total_priority = 0
lines = read_file()

while True:
    try:
        group = [next(lines).strip() for _ in range(3)]
    except StopIteration:
        break
    elf1, elf2, elf3 = group
    badge = list(set(elf1).intersection(elf2).intersection(elf3))[0]
    priority = (ord(badge) - 96) if badge.islower() else (ord(badge) - 38)
    total_priority += priority

print(total_priority)

