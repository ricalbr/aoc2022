# aoc 2022

crates = [  ['Z','J','G'],
            ['Q','L','R','P','W','F','V','C'],
            ['F','P','M','C','L','G','R'],
            ['L','F','B','W','P','H','M'],
            ['G','C','F','S','V','Q'],
            ['W','H','J','Z','M','Q','T','L'],
            ['H','F','S','B','V'],
            ['F','J','Z','S'],
            ['M','C','D','P','F','H','B','T']]

with open('input.txt') as file:
    for line in file:
        l = line.strip().split(' ')
        if l[0] != 'move':
            continue

        num, a, b = int(l[1]), int(l[3]), int(l[5])
        temp = []
        for _ in range(num):
            temp.insert(0, crates[a-1].pop(-1))
        crates[b-1].extend(temp)

res = ''
for stack in crates:
    res+=stack[-1]
print(res)

