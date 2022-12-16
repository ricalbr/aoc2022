from __future__ import annotations

import os.path
import math

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
# INPUT_TXT = os.path.join(os.path.dirname(__file__), 't.txt')

ROUNDS = 10000

def update_item(it_val, op, val):
    if op == 'sm':
        return it_val + val
    elif op == 'pd':
        return it_val * val
    elif op == 'sq':
        return it_val**2
    else:
        raise ValueError(f'{op!r}')



def compute(s: str) -> int:
    monkeys =[]
    monkey = s.split('\n\n')

    WORRY = 1
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
        WORRY *= int(lines[3].rpartition(' by ')[-1])
        mon['next'] = {1: int(lines[4].rpartition('monkey ')[-1]), 0: int(lines[5].rpartition('monkey ')[-1])}
        mon['counter'] = 0
        monkeys.append(mon)


    for i in range(ROUNDS):
        for m in monkeys:
            while m['items']:
                it = m['items'].pop(0)
                m['counter'] += 1
                it = update_item(it, *m['op'])
                it = it % WORRY

                next_monkey = int(it % m['test'] == 0)

                monkeys[m['next'][next_monkey]]['items'].append(it)


    counters = sorted([m['counter'] for m in monkeys], reverse=True)
    return counters[0] * counters[1]



def main() -> int:
    with open(INPUT_TXT) as f:
        print(compute(f.read()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())