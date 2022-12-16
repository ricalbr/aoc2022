from __future__ import annotations

import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

CYCLE = [20, 60, 100, 140, 180, 220]


def compute(s: str) -> int:
    X = []
    x_current = 1

    lines = s.splitlines()
    for line in lines:
        if line == 'noop':
            X.append(x_current)
            continue
        _, val = line.split()
        X.extend([x_current, x_current])
        x_current += int(val)
    X.append(x_current)

    sig_strength = 0
    for cyc in CYCLE:
        sig_strength += cyc * X[cyc - 1]

    return sig_strength


def main() -> int:
    with open(INPUT_TXT) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
