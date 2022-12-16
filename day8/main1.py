# aoc 2022

with open('input.txt', 'r') as f:
    s = f.read()


def compute():
    M = []
    for line in s.split('\n'):
        M.append([int(c) for c in line])
    nr, nc = len(M), len(M[0])

    n_tree = 2 * nr + 2 * (nc - 2)
    for ii in range(1, nr - 1):
        for jj in range(1, nc - 1):
            bot = [M[ii][jj] > M[r][jj] for r in range(ii + 1, nr)]
            top = [M[ii][jj] > M[r][jj] for r in range(0, ii)]
            rig = [M[ii][jj] > M[ii][c] for c in range(jj + 1, nc)]
            lef = [M[ii][jj] > M[ii][c] for c in range(0, jj)]
            if (
                    all(top) or all(bot) or all(rig) or all(lef)
            ):
                n_tree += 1
    return n_tree


if __name__ == '__main__':
    print(compute())
