import math
from os import path
from queue import PriorityQueue

def addOneToMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = []
    for i in range(rows):
        line = []
        for j in range(cols):
            res = matrix[i][j] + 1
            if res > 9:
                res = 1
            line.append(res)
        new_matrix.append(line)
    return new_matrix

def findMinimumRisk(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    graph = {}
    selected = [False] * (rows * cols)
    cost_mat = [math.inf] * (rows * cols)
    for i in range(rows):
        for j in range(cols):
            node_num = i * cols  + j
            graph[node_num] = []
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            for k in range(4):
                dest_x = i + dx[k]
                dest_y = j + dy[k]
                if dest_x < 0 or dest_y < 0 or dest_x >= rows or dest_y >= cols:
                    continue
                cost = matrix[dest_x][dest_y]
                dest = dest_x * cols + dest_y
                graph[node_num].append((cost, dest))
    
    q = PriorityQueue()
    q.put((0, 0))
    cost_mat[0] = 0
    while q.qsize() > 0:
        cost, dest = q.get()
        selected[dest] = True
        for (nod_cost, nod) in graph[dest]:
            if not selected[nod] and cost_mat[nod] > cost_mat[dest] + nod_cost:
                cost_mat[nod] = cost_mat[dest] + nod_cost
                q.put((cost_mat[nod], nod))

    return cost_mat[-1]

def extendMatrix(matrix):
    addedMatrixes = []
    addedMatrixes.append(matrix)
    rows = len(matrix)
    for i in range(1,9):
        addedMatrixes.append(addOneToMatrix(addedMatrixes[i - 1]))
    extendedLines = []
    for i in range(5):
        extendedLine = []
        for j in range(i, i + 5):
            extendedLine.append(addedMatrixes[j])
        extendedLines.append(extendedLine)
    extendedMatrix = []
    for extendedLine in extendedLines:
        for i in range(rows):
            new_line = []
            for j in range(5):
                new_line.extend(extendedLine[j][i])
            extendedMatrix.append(new_line)
    return extendedMatrix


with open('inputs/day15.in') as f:
    lines = f.readlines()
    matrix = []
    for line in lines:
        new_line = line.split('\n')[0]
        new_line = [char for char in new_line]
        new_line = list(map(int, new_line))
        matrix.append(new_line)
    print(findMinimumRisk(matrix))
    extendedMatrix = extendMatrix(matrix)
    print(findMinimumRisk(extendedMatrix))