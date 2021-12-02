def get_position(commands):
    x, y = 0, 0
    for command_str in commands:
        command, units = command_str.split(' ')
        units = int(units)
        if command == "forward":
            x += units
        elif command == "down":
            y += units
        elif command == "up":
            y -= units
    return x * y

def get_positon_with_aim(commands):
    x, y, aim = 0, 0, 0
    for command_str in commands:
        command, units = command_str.split(' ')
        units = int(units)
        if command == "forward":
            x += units
            y += (aim * units)
        elif command == "down":
            aim += units
        elif command == "up":
            aim -= units
    return x * y

with open('inputs/day2.in') as f:
    commands = f.readlines()
    print(get_position(commands))
    print(get_positon_with_aim(commands))
