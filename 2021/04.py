from typing import List

data = ""
with open("2021/04.txt") as f:
    data = f.read().split("\n\n")

drawn = map(int, data[0].split(','))
boards = [
    [
        # {int(x): 0 for x in map(str.strip, row.split()) if x}
        [int(x) for x in map(str.strip, row.split(" ")) if x]
        for row in line.split("\n")
    ]
    for line in data[1:]
]
# splited = [x.split("\n") for x in data[1:]]

# data = []
# for x in splited:
#     l = []
#     for z in x:
#         l.append({int(a): 0 for a in z.split()})
#     data.append(l)

# def findWinner(drawnList, boards):
#     for drawn in drawnList:
#         for i in range(len(boards)):
#             for row in range(len(boards[i])):
#                 if boards[i][row].get(drawn) != None:
#                     boards[i][row][drawn] = 1
#                     if all(v == 1 for v in boards[i][row].values()):
#                         return boards[i], drawn

def solution1(drawnList, boards):
    seen, won, scores = [], [], []
    for n in drawnList:
        seen.append(n)
        for board in boards:
            transpose = list(zip(*board))
            for i, line in enumerate(board):
                if (
                    all(num in seen for num in line)
                    or all(num in seen for num in transpose[i])
                ) and board not in won:
                    won.append(board)
                    scores.append(
                        sum(
                            sum(num for num in line if num not in seen)
                            for line in board
                        )
                        * seen[-1]
                    )
    return scores

scores = solution1(drawn, boards)
print(f'AoC [Day 04][Part 1] Solution: {scores[0]}')
print(f'AoC [Day 04][Part 2] Solution: {scores[-1]}')
# print(f'AoC [Day 03][Part 2] Solution: {solution2(data)}')
