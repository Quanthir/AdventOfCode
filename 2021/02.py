data = ""

with open("2021/02.txt") as f:
    data = f.read().split("\n")

data = [x.split() for x in data]

# print(data)

def solution1(given):
    h = 0
    d = 0

    for x in given:
        if x[0] == "forward":
            h += int(x[1])
        elif x[0] == "up":
            d -= int(x[1])
        elif x[0] == "down":
            d += int(x[1])
    
    return h * d

def solution2(given):
    h = 0
    a = 0
    d = 0

    for x in given:
        if x[0] == "forward":
            h += int(x[1])
            d += int(x[1]) * a
        elif x[0] == "up":
            a -= int(x[1])
        elif x[0] == "down":
            a += int(x[1])
    
    return h * d


print(f'AoC [Day 02][Part 1] Solution: {solution1(data)}')
print(f'AoC [Day 02][Part 2] Solution: {solution2(data)}')
