def getUniqueNumbersCount(lines):
    count = 0
    unique_numbers = [2, 3, 4, 7]
    for line in lines:
        line = line.split(' | ')[1]
        line = line.split('\n')[0]
        numbers = line.split(' ')
        for number in numbers:
            if len(number) in unique_numbers:
                count += 1
    return count

def sortString(str):
    return ''.join(sorted(str))

#   l3l3              l3l3     l3l3                l3l3      l3l3    l3l3       l3l3      l3l3
# l5    l1      l1       l1       l1  l5    l1  l5        l5            l1   l5    l1  l5    l1
# l5    l1      l1       l1       l1  l5    l1  l5        l5            l1   l5    l1  l5    l1
#                     l4l4     l4l4     l4l4      l4l4      l4l4               l4l4      l4l4
# l6    l2      l2  l6            l2        l2        l2  l6    l2      l2   l6    l2        l2
# l6    l2      l2  l6            l2        l2        l2  l6    l2      l2   l6    l2        l2
#   l7l7              l7l7     l7l7                l7l7      l7l7               l7l7      l7l7

def findPins(entry):
    (patterns, outputs) = entry.split(' | ')
    patterns = patterns.split(' ')
    outputs = outputs.split('\n')[0]
    outputs = outputs.split(' ')
    number_patterns = [None] * 10
    patterns_map = {}
    six_letter_patterns = []
    l1,l2,l3,l4,l5,l6,l7 = [None] * 7
    for pattern in patterns:
        pattern = sortString(pattern)
        if len(pattern) == 2:
            patterns_map[pattern] = 1
            number_patterns[1] = pattern
        elif len(pattern) == 3:
            patterns_map[pattern] = 7
            number_patterns[7] = pattern
        elif len(pattern) == 4:
            patterns_map[pattern] = 4
            number_patterns[4] = pattern
        elif len(pattern) == 7:
            patterns_map[pattern] = 8
            number_patterns[8] = pattern
        elif len(pattern) == 6:
            pattern
            six_letter_patterns.append(pattern)
    l3 = list(filter(lambda letter: letter not in number_patterns[1], number_patterns[7]))[0]
    l4l5 = list(filter(lambda letter: letter not in number_patterns[1], number_patterns[4]))
    l3l6l7 = list(filter(lambda letter: letter not in number_patterns[4], number_patterns[8]))
    l6l7 = list(filter(lambda letter: letter != l3, l3l6l7))
    for six_letter_pattern in six_letter_patterns:
        unkonwn_letter = list(filter(lambda letter: letter not in six_letter_pattern, number_patterns[8]))[0]
        if unkonwn_letter in l4l5:
            l4 = unkonwn_letter
            l5 = list(filter(lambda letter: letter != l4, l4l5))[0]
            patterns_map[six_letter_pattern] = 0
            
        elif unkonwn_letter in l6l7:
            l6 = unkonwn_letter
            l7 = list(filter(lambda letter: letter != l6, l6l7))[0]
            patterns_map[six_letter_pattern] = 9

        else:
            l1 = unkonwn_letter
            l2 = list(filter(lambda letter: letter != l1, number_patterns[1]))[0]
            patterns_map[six_letter_pattern] = 6
    patterns_map[sortString(l1 + l3 + l4 + l6 + l7)] = 2
    patterns_map[sortString(l1 + l2 + l3 + l4 + l7)] = 3
    patterns_map[sortString(l2 + l3 + l4 + l5 + l7)] = 5
    number = 0
    
    for output in outputs:
        output = sortString(output)
        number *= 10
        number += patterns_map[output]
    return number

def getSumOfAllEncodedNumbers(encodedLines):
    sum = 0
    for line in encodedLines:
        sum += findPins(line)
    return sum

with open('inputs/day8.in') as f:
    lines = f.readlines()
    print(getUniqueNumbersCount(lines))
    print(getSumOfAllEncodedNumbers(lines))