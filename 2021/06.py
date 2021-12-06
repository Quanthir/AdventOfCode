
with open('2021/06.txt') as f:
    data = f.read()

data2 = [int(x) for x in data.split(',')]

def solution1(fishes, days=80):
    for i in range(days):
        for f in range(len(fishes)):
            fishes[f] -= 1

            if fishes[f] == 0:
                fishes[f] = 7
                fishes.append(9)
    
    return sum(1 for x in fishes if x < 9)

def solution2(data: list, days: int) -> int:
    s = ''.join(data)
    f = [*map(s.count, '012345678')]

    for _ in range(days):
        f = f[1:] + f[:1]
        f[6] += f[-1]
    
    return sum(f)

print(f'AoC [Day 06][Part 1] Solution: {solution2(data,  80)}')
print(f'AoC [Day 06][Part 2] Solution: {solution2(data, 256)}')

