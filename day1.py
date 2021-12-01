def get_larger_measurments(measurements):
    larger_measurments = 0
    for i in range(1, len(measurements)):
        if (measurements[i] > measurements[i - 1]):
            larger_measurments += 1
    return larger_measurments

def get_larger_sums(measurements):
    larger_sums = 0
    sums = []
    for i in range(0, len(measurements) - 2):
        sums.append(sum(measurements[i:i+3]))
    for i in range(1, len(sums)):
        if (sums[i] - sums[i - 1] > 0):
            larger_sums += 1
    return larger_sums

with open('inputs/day1.in') as f:
    measurements = [int(line.strip()) for line in f]
    print(get_larger_measurments(measurements))
    print(get_larger_sums(measurements))
