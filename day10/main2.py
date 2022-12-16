from __future__ import annotations

import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

CYCLE = [20, 60, 100, 140, 180, 220]


def compute(s: str) -> str:
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

    screen = []
    for i, x_val in enumerate(X):
        sprite_pos = [x_val - 1, x_val, x_val + 1]
        row, col = i // 40, i % 40
        if col == 0:
            screen.append('\n')
        if col in sprite_pos:
            screen.append('o')
        else:
            screen.append(' ')
    return ''.join(screen)


def main() -> int:
    with open(INPUT_TXT) as f:
        print(compute(f.read()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
