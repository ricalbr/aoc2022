# aoc 2022

with open('input.txt', 'r') as f:
    s = f.read()


def compute():
    M = []
    for line in s.split('\n'):
        M.append([int(c) for c in line])
    nr, nc = len(M), len(M[0])

    max_view = 0
    for ii in range(1, nr - 1):
        for jj in range(1, nc - 1):
            bot = [M[r][jj] for r in range(ii + 1, nr)]
            top = list(reversed([M[r][jj] for r in range(0, ii)]))
            rig = [M[ii][c] for c in range(jj + 1, nc)]
            lef = list(reversed([M[ii][c] for c in range(0, jj)]))

            n_tree = 1
            for lst in [bot, top, rig, lef]:
                tmp = 0
                for tree in lst:
                    if tree < M[ii][jj]:
                        tmp += 1
                    elif tree >= M[ii][jj]:
                        tmp += 1
                        break
                n_tree *= tmp
            max_view = max(max_view, n_tree)
    return max_view


if __name__ == '__main__':
    print(compute())
