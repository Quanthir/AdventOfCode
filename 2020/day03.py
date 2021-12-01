from functools import reduce

data = ""

with open("2020/day03.txt") as f:
    data = f.read().split("\n")

def solution1(d, right, down):
    x, y, count = 0, 0, 0
    while y < len(d) - 1:
        y += down
        x = (x + right) % len(d[y])
        
        if d[y][x] == '#':
            count += 1

    return count


def solution2(d):
    pattern = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    return reduce(lambda a, b: a * solution1(d, b[0], b[1]), pattern, 1)


print(f'AoC [Day 03][Part 1] Solution: {solution1(data, 3, 1)}')
print(f'AoC [Day 03][Part 2] Solution: {solution2(data)}')
