# aoc day2

# opponent moves vs response points mappings
R = dict(X=3+1, Y=6+2, Z=0+3)
P = dict(X=0+1, Y=3+2, Z=6+3)
S = dict(X=6+1, Y=0+2, Z=3+3)

# possible opponent moves
moves = dict(A=R, B=P, C=S)

total_points = 0
with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        opp, response = line.strip().split(' ')
        total_points += moves[opp][response]
print(total_points)
