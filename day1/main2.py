# aoc day 1

calories = []
temp_sum = 0
with open('input1.txt', 'r') as file:
    for line in file:
        if line == '\n':
            calories.append(temp_sum)
            temp_sum = 0
        else:
            temp_sum += int(line.strip())
print(sum(sorted(calories)[-3:]))
