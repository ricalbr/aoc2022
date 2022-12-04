# aoc2022
from __future__ import annotations

def get_set(task:list[str]) -> set[int]:
    section = [int(sec) for sec in task.split('-')]
    return set(range(section[0], section[-1]+1))

total_overlap = 0

with open('input.txt', 'r') as f:
    for line in f:
        pair = line.strip().split(',')
        task1, task2 = pair
        set1 = get_set(task1)
        set2 = get_set(task2)
        if set1.intersection(set2):
            total_overlap += 1
print(total_overlap)

