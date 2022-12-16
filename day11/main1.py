from __future__ import annotations

import math
import os.path

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')

ROUNDS = 20


def update_item(it_val, op, val):
    if op == 'sm':
        return it_val + val
    elif op == 'pd':
        return it_val * val
    elif op == 'sq':
        return it_val ** 2
    else:
        raise ValueError(f'{op!r}')


def compute(s: str) -> int:
    monkeys = []
    monkey = s.split('\n\n')
    for m in monkey:
        lines = m.splitlines()
        mon = {}
        i_list = lines[1].rpartition(': ')[-1].split(', ')
        mon['items'] = [int(elem) for elem in i_list]

        if lines[2].rpartition(' + ')[1] == ' + ':
            mon['op'] = 'sm', int(lines[2].rpartition(' + ')[-1])
        else:
            try:
                mon['op'] = 'pd', int(lines[2].rpartition(' * ')[-1])
            except ValueError:
                mon['op'] = 'sq', int(2)

        mon['test'] = int(lines[3].rpartition(' by ')[-1])
        mon['next'] = {1: int(lines[4].rpartition('monkey ')[-1]), 0: int(lines[5].rpartition('monkey ')[-1])}
        mon['counter'] = 0
        monkeys.append(mon)

    for i in range(ROUNDS):
        for m in monkeys:
            while m['items']:
                it = m['items'].pop(0)
                m['counter'] += 1
                it = update_item(it, *m['op'])
                it = int(math.ceil(it // 3))

                monkeys[m['next'][int(it % m['test'] == 0)]]['items'].append(it)

    counters = sorted([m['counter'] for m in monkeys], reverse=True)
    print(counters)
    return counters[0] * counters[1]


def main() -> int:
    with open(INPUT_TXT) as f:
        print(compute(f.read()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
