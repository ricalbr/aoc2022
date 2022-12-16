# aoc 2022

with open('input.txt', 'r') as f:
    s = f.read()


def cumsize(tree, root):
    if not tree[root]['subd']:
        return tree[root]['s']
    else:
        children = ['-'.join([root, c]) for c in tree[root]['subd']]
        return tree[root]['s'] + sum([cumsize(tree, c) for c in children])


def compute():
    tree = {}
    path = []
    TOTAL_SPACE = 70_000_000
    UPDATE_SPACE = 30_000_000

    lst = s.strip('\n').replace('$ ls', '').replace('$ cd ', '\t')
    for branch in lst.split('\t'):
        if branch in ['', '\n']:
            continue
        elif branch.strip() == '..':
            path.pop()
        elif len(branch.strip()) == 1:
            dire = branch.strip()
            if dire == '/':
                path = ['/']
            else:
                path.extend(branch.strip())
        else:
            dr, content = branch.split('\n\n')
            content = sorted(content.strip().split('\n'))
            path.append(dr)
            dr = '-'.join(path)
            subdirs = []
            files = []
            for elem in content:
                if elem.split(' ')[0] == 'dir':
                    subdirs.append(elem.split(' ')[-1])
                else:
                    files.append(int(elem.split(' ')[0]))
            tree[dr] = dict(s=sum(files), subd=subdirs)

    REQUIRED_SPACE = UPDATE_SPACE - (TOTAL_SPACE - cumsize(tree, '/'))

    if REQUIRED_SPACE <= 0:
        return 0

    min_size = TOTAL_SPACE
    for k, e in tree.items():
        tmp_s = cumsize(tree, k)
        if tmp_s > REQUIRED_SPACE:
            min_size = min(min_size, tmp_s)
    return min_size


if __name__ == '__main__':
    print(compute())
