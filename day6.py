def get_fishes_after_days(times, days):
    for day in range(days):
        new_fishes = 0
        for i in range(len(times)):
            if times[i] == 0:
                times[i] = 6
                new_fishes += 1
            else:
                times[i] -= 1
        for _ in range(new_fishes):
            times.append(8)
    return len(times)

def get_fishes_after_days_opt(times, days):
    days_left = [0] * 9
    for time in times:
        days_left[time] += 1
    for day in range(days):
        fishes_done = days_left[0]
        for i in range(1, len(days_left)):
            days_left[i - 1] = days_left[i]
        days_left[8] = fishes_done
        days_left[6] += fishes_done
    return sum(days_left)

with open('inputs/day6.in') as f:
    initial_times = list(map(int,f.read().split(',')))
    times = initial_times.copy()
    print(get_fishes_after_days(times, 80))
    times = initial_times.copy()
    print(get_fishes_after_days_opt(times, 256))