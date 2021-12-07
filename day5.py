from collections import defaultdict

def get_points_with_overlap(vents):
    points = defaultdict(lambda: 0)
    for vent in vents:
        (x_start, y_start) = vent[0]
        (x_end, y_end) = vent[1]
        if x_start == x_end:
            if y_start > y_end:
                y_start, y_end = y_end, y_start
            for col in range(y_start, y_end + 1):
                points[(x_start, col)] += 1
        if y_start == y_end:
            if x_start > x_end:
                x_start, x_end = x_end, x_start
            for row in range(x_start, x_end + 1):
                points[(row, y_start)] += 1
    overlaps = list(points.values())
    overlaps = list(filter(lambda x: x > 1, overlaps))
    return len(overlaps)

def get_points_with_diag_overlaps(vents):
    points = defaultdict(lambda: 0)
    for vent in vents:
        (x_start, y_start) = vent[0]
        (x_end, y_end) = vent[1]
        if x_start == x_end:
            if y_start > y_end:
                y_start, y_end = y_end, y_start
            for col in range(y_start, y_end + 1):
                points[(x_start, col)] += 1
        elif y_start == y_end:
            if x_start > x_end:
                x_start, x_end = x_end, x_start
            for row in range(x_start, x_end + 1):
                points[(row, y_start)] += 1
        elif x_start == y_start and x_end == y_end:
            if x_start > x_end:
                x_start, x_end = x_end, x_start
            for row in range(x_start, x_end + 1):
                points[(row, row)] += 1
        else:
            if x_start > x_end:
                x_start, x_end = x_end, x_start
                y_start, y_end = y_end, y_start
            for x in range(x_start, x_end + 1):
                if y_end > y_start:
                    y = y_start + (x - x_start)
                else:
                    y = y_start - (x - x_start)
                points[(x, y)] += 1
    overlaps = list(points.values())
    overlaps = list(filter(lambda x: x > 1, overlaps))
    return len(overlaps)

with open('inputs/day5.in') as f:
    lines = f.readlines()
    vents = []
    for line in lines:
        (start, end) = line.split('->')
        start = start.split('\n')[0]
        end = end.split('\n')[0]
        start = tuple(map(int, start.split(',')))
        end = tuple(map(int, end.split(',')))
        vents.append((start, end))
    print(get_points_with_overlap(vents))
    print(get_points_with_diag_overlaps(vents))