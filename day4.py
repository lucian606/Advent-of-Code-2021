from collections import defaultdict

def checkWin(board, boardMap):
    for i in range(len(board)):
        count_line = 0
        count_column = 0
        for j in range(len(board[i])):
            if boardMap[(i, j)] == 1:
                count_line += 1
            if boardMap[(j, i)] == 1:
                count_column += 1
        if count_line == len(board[i]) or count_column == len(board[i]):
            return True
    return False

def getCoordOfNumber(board, number):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == number:
                return (i, j)
    return (-1, -1)

def calculate_score(boards, coordsMaps, numbers):
    for number in numbers:
        for i in range(len(boards)):
            (row, col) = getCoordOfNumber(boards[i], number)
            if row != -1:
                coordsMaps[i][(row, col)] = 1
            sum = 0
            if checkWin(boards[i], coordsMaps[i]):
                for row in range(len(boards[i])):
                    for col in range(len(boards[i][row])):
                        if coordsMaps[i][(row, col)] == 0:
                            sum += boards[i][row][col]
                return number * sum
    return 0

def get_final_board_scoare(boards, coordsMaps, numbers):
    won_boards = defaultdict(lambda: 0)
    won_count = 0
    for number in numbers:
        for i in range(len(boards)):
            (row, col) = getCoordOfNumber(boards[i], number)
            if row != -1:
                coordsMaps[i][(row, col)] = 1
            if checkWin(boards[i], coordsMaps[i]) and not won_boards[i]:
                won_count += 1
                won_boards[i] = True
                if won_count == len(boards):
                    sum = 0
                    for row in range(len(boards[i])):
                        for col in range(len(boards[i][row])):
                            if coordsMaps[i][(row, col)] == 0:
                                sum += boards[i][row][col]
                    return number * sum
    return 0

with open('inputs/day4.in') as f:
    numbers = list(map(int, (f.readline()).split(',')))
    lines = f.readlines()
    boards = []
    coodsMaps = []
    for i in range(0, len(lines), 6):
        board = []
        for k in range(1, 6):
            line = lines[i+k].split('\n')[0].split(' ')
            line = list(filter(lambda x: x != '', line))
            line = list(map(int, line))
            board.append(line)
        coodsMaps.append(defaultdict(lambda: 0))
        boards.append(board)
    print(calculate_score(boards, coodsMaps, numbers))
    print(get_final_board_scoare(boards, coodsMaps, numbers))