data = ""

with open("2020/day01.txt") as f:
    data = [int(i) for i in f.read().split()]

def solution1(d):
    for x in d:
        for y in d:
            if x + y == 2020:
                return x * y

def solution2(d):
    for x in d:
        for y in d:
            for z in d:
                if x + y + z == 2020:
                    return x * y * z


print(f'AoC [Day 01][Part 1] Solution: {solution1(data)}')
print(f'AoC [Day 01][Part 2] Solution: {solution2(data)}')
