from os import error


def get_error_score(lines):
    scores = {')':3, ']':57, '}':1197, '>':25137}
    closing = {'(':')', '[':']', '{':'}', '<':'>'}
    error_score = 0
    opening_brakets = "([{<"
    for line in lines:
        line = line.split('\n')[0]
        stack = []
        for braket in line:
            if braket in opening_brakets:
                stack.append(braket)
            else:
                if len(stack) == 0:
                    error_score += scores[braket]
                    break
                opening_braket = stack.pop()
                if closing[opening_braket] != braket:
                    error_score += scores[braket]
                    break
    return error_score

def get_incomplete_score(lines):
    scores = {'(':1, '[':2, '{':3, '<':4}
    closing = {'(':')', '[':']', '{':'}', '<':'>'}
    opening_brakets = "([{<"
    incomplete_scores = []
    for line in lines:
        line = line.split('\n')[0]
        stack = []
        isErrorLine = False
        for braket in line:
            if braket in opening_brakets:
                stack.append(braket)
            else:
                if len(stack) == 0:
                    isErrorLine = True
                    break
                opening_braket = stack.pop()
                if closing[opening_braket] != braket:
                    isErrorLine = True
                    break
        if not isErrorLine and len(stack):
            score = 0
            stack.reverse()
            for braket in stack:
                score *= 5
                score += scores[braket]
            incomplete_scores.append(score)
    incomplete_scores.sort()
    middle = len(incomplete_scores) // 2 
    return incomplete_scores[middle]

with open('inputs/day10.in') as f:
    lines = f.readlines()
    print(get_error_score(lines))
    print(get_incomplete_score(lines))