def get_power_consumption(bin_numbers):
    bits = len(bin_numbers[-1])
    bin_gamma = "0" * bits
    for bit in range(bits):
        count = 0
        for number in bin_numbers:
            if number[bit] == "1":
                count += 1
            else:
                count -= 1
        if count > 0:
            bin_gamma = bin_gamma[:bit] + "1" + bin_gamma[bit+1:]
    bin_epsilon = ''.join(["0" if bit == "1" else "1" for bit in bin_gamma])
    epsilon = int(bin_epsilon, 2)
    gamma = int(bin_gamma, 2)
    return gamma * epsilon

def get_oxygen_rating(bin_numbers):
    bits = len(bin_numbers[-1])
    for bit in range(bits):
        count = 0
        dominant_bit = "0"
        for number in bin_numbers:
            if number[bit] == "1":
                count += 1
            else:
                count -= 1
        if count >= 0:
            dominant_bit = "1"
        bin_numbers = list(filter(lambda x: x[bit] == dominant_bit, bin_numbers))
        if len(bin_numbers) == 1:
            return int(bin_numbers[0], 2)

def get_CO2_rating(bin_numbers):
    bits = len(bin_numbers[-1])
    for bit in range(bits):
        count = 0
        least_bit = "0"
        for number in bin_numbers:
            if number[bit] == "1":
                count += 1
            else:
                count -= 1
        if count < 0:
            least_bit = "1"
        bin_numbers = list(filter(lambda x: x[bit] == least_bit, bin_numbers))
        if len(bin_numbers) == 1:
            return int(bin_numbers[0], 2)


with open('inputs/day3.in') as f:
    bin_numbers = f.readlines()
    print(get_power_consumption(bin_numbers))
    print(get_oxygen_rating(bin_numbers) * get_CO2_rating(bin_numbers))