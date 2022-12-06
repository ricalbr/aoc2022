# aoc 2022

with open('input.txt', 'r') as f:
    s = f.readline().strip()


def compute():
    window = list(s[:3].strip())

    for i, c in enumerate(s[3:]):
        window.append(c)
        if len(window) > 4:
            window.pop(0)

        sum_occ = sum([window.count(elem) for elem in window])
        if sum_occ != 4:
            continue
        else:
            return i + 4


if __name__ == '__main__':
    print(compute())
