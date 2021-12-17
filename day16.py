from functools import reduce

version_sum = 0

def eval_packet(packet, pos):
    global version_sum
    i = pos[0]
    version = packet[i: i + 3]
    version_sum += int(version, 2)
    type_id = packet[i + 3: i + 6]
    i += 6
    values = []

    if type_id == "100":
        value = ""
        while True:
            group = packet[i]
            i += 1
            chunk = packet[i : i + 4]
            i += 4
            value += chunk
            if group == "0":
                break
        pos[0] = i
        return int(value, 2)

    if packet[i] == '0':
        i += 1
        length = int(packet[i : i + 15], 2)
        i += 15
        values_end = length + i
        pos[0] = i
        while pos[0] != values_end:
            values.append(eval_packet(packet, pos))
    else:
        i += 1
        packets_num = int(packet[i:i + 11], 2)
        i += 11
        pos[0] = i
        for _ in range(packets_num):
            values.append(eval_packet(packet, pos))
    
    if type_id == "000":
        return sum(values)
    elif type_id == "001":
        return reduce(lambda a,b: a * b, values)
    elif type_id == "010":
        return min(values)
    elif type_id == "011":
        return max(values)
    elif type_id == "101":
        return int(values[0] > values[1])
    elif type_id == "110":
        return int(values[0] < values[1])
    elif type_id == "111":
        return int(values[0] == values[1])

def hex_to_bin(hex_str):
    bin = ""
    for chr in hex_str:
        num = int(chr, 16)
        bin += '{0:04b}'.format(num)
    return bin

with open('./inputs/day16.in') as f:
    input_str = f.read()
    bin_packet = hex_to_bin(input_str)
    pos = [0]
    res = eval_packet(bin_packet, pos)
    print(version_sum)
    print(res)