import re

data = ""

with open("2020/day02.txt") as f:
    data = f.read().split("\n")

data = [re.match(r'(\d+)-(\d+) (\w): (\w+)', x).groups() for x in data]
data = [[int(x[0]), int(x[1]), x[2], x[3]] for x in data]

def solution1(d):
    return sum(x[0] <= x[3].count(x[2]) <= x[1] for x in data)

def solution2(d):
    puz = lambda pos1, pos2, c, s: (s[pos1] == c or s[pos2] == c) and s[pos1] != s[pos2]
    # for x in d:
    #     print(x[0], x[1], x[2], x[3], end=" = ")
    #     print(puz(x[0]-1, x[1]-1, x[2], x[3]))
    return sum(puz(x[0]-1, x[1]-1, x[2], x[3]) for x in d)


print(f'AoC [Day 02][Part 1] Solution: {solution1(data)}')
print(f'AoC [Day 02][Part 2] Solution: {solution2(data)}')
