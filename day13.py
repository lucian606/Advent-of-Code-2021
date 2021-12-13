from collections import defaultdict

def executeFold(paper, fold):
    axis, amount = fold
    amount = int(amount)
    if axis == 'x':
        keys_to_remove = []
        keys_to_add = []
        for key in paper.keys():
            i, j = key
            if i > amount:
                delta = i - amount
                keys_to_remove.append((i, j))
                keys_to_add.append((amount - delta, j))
            if i == amount:
                keys_to_remove.append((i, j))
        for key in keys_to_remove:
            paper.pop(key)
        for key in keys_to_add:
            paper[key] = '█'
    else:
        keys_to_remove = []
        keys_to_add = []
        for key in paper.keys():
            i, j = key
            if j > amount:
                delta = j - amount
                keys_to_remove.append((i, j))
                keys_to_add.append((i, amount - delta))
            if j == amount:
                keys_to_remove.append((i, j))
        for key in keys_to_remove:
            paper.pop(key)
        for key in keys_to_add:
            paper[key] = '█'

with open('inputs/day13.in') as f:
    lines = f.readlines()
    folds = []
    paper = defaultdict(lambda: ".")    
    for line in lines:
        if line == '\n':
            continue
        elif "fold" in line:
            line = line.split('\n')[0]
            fold_info = line.split(' ')[2]
            axis, amount = fold_info.split('=')
            folds.append((axis, amount))
        else:
            line = line.split('\n')[0]
            x, y = line.split(',')
            x, y = int(x), int(y)
            paper[(x, y)] = '█'
    for i in range(len(folds)):
        executeFold(paper, folds[i])
        if (i == 0):
            print(len(paper.keys()))
    rows, cols = 0, 0
    for key in paper.keys():
        x, y = key
        if x > cols:
            cols = x
        if y > rows:
            rows = y
    rows += 1
    cols += 1
    for i in range(rows):
        for j in range(cols):
            print(paper[(j, i)], end='')
        print()