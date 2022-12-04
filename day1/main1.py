# aoc day 1

temp_max = 0
temp_sum = 0
with open('input1.txt', 'r') as file:
    for line in file:
        if line == '\n':
            temp_max = max([temp_max, temp_sum])
            temp_sum = 0
        else:
            temp_sum += int(line.strip())
print(temp_max)
