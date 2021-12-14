from collections import defaultdict

def applyRules(template, rules):
    rulesmap =  defaultdict(lambda: None)
    for rule in rules:
        pair, letter = rule.split(' -> ')
        rulesmap[pair] = letter
    i = 0
    while True:
        if i == len(template) or i == len(template) - 1:
            break
        else:
            pair = template[i] + template[i + 1]
            if rulesmap[pair]:
                template = template[:i + 1] + rulesmap[pair] + template[i + 1:]
                i += 2
            else:
                i += 1
    return template

def getMostAndLeastDiff(str):
    charsCount = defaultdict(lambda: 0)
    for c in str:
        charsCount[c] += 1
    tmp = list(charsCount.values())
    tmp.sort()
    return(tmp[-1] - tmp[0])

def getDiffFast(template, rules):
    rulesmap =  defaultdict(lambda: None)
    for rule in rules:
        pair, letter = rule.split(' -> ')
        rulesmap[pair] = letter
    current_pairs = defaultdict(lambda: 0)
    charsCount = defaultdict(lambda: 0)
    
    for i in range(len(template)):
        if i + 1 != len(template):
            pair = template[i:i+2]
            current_pairs[pair] += 1
        charsCount[template[i]] += 1
    
    for _ in range(40):
        new_pairs = defaultdict(lambda: 0)

        for pair in current_pairs:
            new_char = rulesmap[pair]

            pair_one = pair[0] + new_char
            pair_two = new_char + pair[1]

            new_pairs[pair_one] += current_pairs[pair]
            new_pairs[pair_two] += current_pairs[pair]


            charsCount[new_char] += current_pairs[pair]

        current_pairs = new_pairs

    return(max(charsCount.values())- min(charsCount.values()))

with open('inputs/day14.in') as f:
    lines = f.readlines()
    template = None
    rules = []
    for i in range(len(lines)):
        if i == 0:
            template = lines[i].split('\n')[0]
        elif lines[i] == "\n":
            continue
        else:
            rule = lines[i].split('\n')[0]
            rules.append(rule)
    old_template = template
    for _ in range(10):
        template = applyRules(template, rules)
    print(getMostAndLeastDiff(template))
    template = old_template
    print(getDiffFast(template, rules))