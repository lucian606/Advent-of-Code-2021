def get_minimum_cost(positions):
    positions.sort()
    min_cost = float('inf')
    for position in positions:
        cost = 0
        for i in range(len(positions)):
            cost += abs(position - positions[i])
        if cost < min_cost:
            min_cost = cost
    return min_cost

def get_minimum_cost_non_constant_rate(positions):
    positions.sort()
    min_cost = float('inf')
    for position in positions:
        cost = 0
        for i in range(len(positions)):
            delta = abs(position - positions[i])
            cost += delta * (delta + 1) / 2
        if cost < min_cost:
            min_cost = cost
    return min_cost

with open('inputs/day7.in') as f:
    positions = list(map(int,f.read().split(',')))
    print(get_minimum_cost(positions))
    print(get_minimum_cost_non_constant_rate(positions))