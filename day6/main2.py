# aoc 2022

with open('input.txt', 'r') as f:
    s = f.readline().strip()


def compute():
    window = list(s[:13].strip())

    for i, c in enumerate(s[13:]):
        window.append(c)
        if len(window) > 14:
            window.pop(0)

        sum_occ = sum([window.count(elem) for elem in window])
        if sum_occ != 14:
            continue
        else:
            return i + 14


if __name__ == '__main__':
    print(compute())
