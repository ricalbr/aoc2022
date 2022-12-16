from __future__ import annotations

import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:

    lines = s.splitlines()
    for line in lines:
        pass
    # TODO: solution here!
    return 0


def main() -> int:
    with open(INPUT_TXT) as f:
        print(compute(f.read()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
