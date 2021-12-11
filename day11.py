from collections import defaultdict
from copy import copy, deepcopy

def flashCell(lines, i, j, flashed_cells):
    rows = len(lines)
    cols = len(lines[0])
    if (
        i < 0 or
        j < 0 or
        i >= rows or
        j >= cols
    ):
        return
    else:
        lines[i][j] += 1
        if lines[i][j] > 9 and not flashed_cells[(i, j)]:
            flashed_cells[(i, j)] = True
            flashCell(lines, i + 1, j, flashed_cells)
            flashCell(lines, i - 1, j, flashed_cells)            
            flashCell(lines, i, j + 1, flashed_cells)
            flashCell(lines, i, j - 1, flashed_cells)
            flashCell(lines, i + 1, j + 1, flashed_cells)            
            flashCell(lines, i + 1, j - 1, flashed_cells)
            flashCell(lines, i - 1, j + 1, flashed_cells)            
            flashCell(lines, i - 1, j - 1, flashed_cells)

def getNumberOfFlashes(lines, steps):
    rows = len(lines)
    cols = len(lines[0])
    flashes = 0
    
    for _ in range(steps):
        flashed_cells = defaultdict(lambda: False)

        for i in range(rows):
            for j in range(cols):
                lines[i][j] += 1

        for i in range(rows):
            for j in range(cols):
                if lines[i][j] > 9 and not flashed_cells[(i,j)]:
                    flashCell(lines, i, j, flashed_cells)

        for (i, j) in flashed_cells.keys():
            if flashed_cells[(i, j)]:
                lines[i][j] = 0
                flashes += 1
    return flashes

def getFirstFullFlashStep(lines):
    rows = len(lines)
    cols = len(lines[0])
    step = 0

    while True:
        step += 1
        flash_count = 0
        
        flashed_cells = defaultdict(lambda: False)

        for i in range(rows):
            for j in range(cols):
                lines[i][j] += 1

        for i in range(rows):
            for j in range(cols):
                if lines[i][j] > 9 and not flashed_cells[(i,j)]:
                    flashCell(lines, i, j, flashed_cells)

        for (i, j) in flashed_cells.keys():
            if flashed_cells[(i, j)]:
                lines[i][j] = 0
                flash_count += 1
        
        if flash_count == rows * cols:
            return step

with open('inputs/day11.in') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split('\n')[0]
        lines[i] = list(map(int, lines[i]))
    old_lines = deepcopy(lines)
    print(getNumberOfFlashes(lines, 100))
    print(getFirstFullFlashStep(old_lines))