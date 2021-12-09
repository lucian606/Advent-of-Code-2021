VISITED = 10

def getBasinSize(heightmap, i, j):
    rows = len(heightmap)
    cols = len(heightmap[0])
    if (
        i == rows or
        i == -1 or
        j == cols or
        j == -1 or
        heightmap[i][j] >= 9
    ):
        return 0
    else:
        heightmap[i][j] = VISITED
        return (1 + 
            getBasinSize(heightmap, i + 1, j) +
            getBasinSize(heightmap, i - 1, j) +
            getBasinSize(heightmap, i, j - 1) +
            getBasinSize(heightmap, i, j + 1))
    

def getLowPointsRisk(heightmap):
    risk = 0
    rows = len(heightmap)
    cols = len(heightmap[0])
    for i in range(rows):
        for j in range(cols):
            if (
                (i == 0 or heightmap[i][j] < heightmap[i - 1][j])
                and (i == rows - 1 or heightmap[i][j] < heightmap[i + 1][j])
                and (j == 0 or heightmap[i][j] < heightmap[i][j - 1])
                and (j == rows - 1 or heightmap[i][j] < heightmap[i][j + 1])
            ):
                risk += (heightmap[i][j] + 1)
    return risk

def getTopThreeBasins(heightmap):
    rows = len(heightmap)
    cols = len(heightmap[0])
    basin_sizes = []
    for i in range(rows):
        for j in range(cols):
            if heightmap[i][j] != 9:
                basin_sizes.append(getBasinSize(heightmap, i, j))
    basin_sizes.sort(reverse = True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


with open('inputs/day9.in') as f:
    lines = f.readlines()
    heightmap = []
    for line in lines:
        line = line.strip()
        line = list(map(int, line))
        heightmap.append(line)
    print(getLowPointsRisk(heightmap))
    print(getTopThreeBasins(heightmap))
