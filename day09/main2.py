from __future__ import annotations

import os.path

# INPUT_TXT = os.path.join(os.path.dirname(__file__), 't.txt')
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

def move_tail(head, tail):
    dx = head['x'] - tail['x']
    dy = head['y'] - tail['y']
    if abs(dx) <= 1 and abs(dy) <= 1:
        return tail
    if abs(dy) == 0:
        tail['x'] = tail['x'] - 1 if dx < 0 else tail['x'] + 1
        return tail
    if abs(dx) == 0:
        tail['y'] = tail['y'] - 1 if dy < 0 else tail['y'] + 1
        return tail

    tail['x'] = tail['x'] - 1 if dx < 0 else tail['x'] + 1
    tail['y'] = tail['y'] - 1 if dy < 0 else tail['y'] + 1
    return tail

KNOTS = 10

def compute(s: str) -> int:
    old_rope = [dict(x=0, y=0) for _ in range(KNOTS)]
    visited = [(0,0)]

    lines = s.splitlines()
    for line in lines:
        direction, niter = line.split()
        for _ in range(int(niter)):
            H = old_rope.pop(0)

            if direction == 'R':
                H['x'] += 1
            if direction == 'L':
                H['x'] -= 1
            if direction == 'U':
                H['y'] += 1
            if direction == 'D':
                H['y'] -= 1
            new_rope = [H]
            for knot in old_rope:
                new_knot = move_tail(new_rope[-1], knot)
                new_rope.append(new_knot)
            pos_T = (new_rope[-1]['x'], new_rope[-1]['y'])
            if pos_T not in visited:
                visited.append(pos_T)
            old_rope = new_rope
    return len(visited)


def main() -> int:
    with open(INPUT_TXT) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
