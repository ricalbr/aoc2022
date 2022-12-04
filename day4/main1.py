# aoc2022

total_overlap = 0

with open('input.txt', 'r') as f:
    for line in f:
        pair = line.strip().split(',')
        task1, task2 = pair
        sections1 = [int(sec) for sec in task1.split('-')]
        sections2 = [int(sec) for sec in task2.split('-')]
        if (sections1[0] <= sections2[0] and sections1[1] >= sections2[1]):
            total_overlap += 1
        elif(sections2[0] <= sections1[0] and sections2[1] >= sections1[1]):
            total_overlap += 1
        else:
            continue
print(total_overlap)

