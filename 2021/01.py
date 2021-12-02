depths = ""

with open("2021/01.txt") as f:
    depths = [int(i) for i in f.read().split()]

def p1_solution_1(d):
    prev = d[0]
    count = 0
    for x in d:
        if x > prev:
            count += 1
        prev = x

    return count

def p1_solution_2(d):
    return sum(d[i + 1] > d[i] for i in range(len(d) - 1))
    # return reduce(lambda a, b: a + 1 if b > a else 0, depths)


def p2_solution_1(d):
    last = d[0] + d[1] + d[2]
    i = 1
    count = 0
    while True:
        if i + 2 == len(d):
            break

        s = d[i] + d[i + 1] + d[i + 2]
        s = sum(d[i:i+3])
        if s > last:
            count += 1
        
        last = s

        i += 1
    return count

def p2_solution_2(d):
    chunk = [a + b + c for a, b, c in zip(d, d[1::], d[2::])]
    return p1_solution_2(chunk)


print(f'AoC [Day 01][Part 1] Solution 1: {p1_solution_1(depths)} | Solution 2: {p1_solution_2(depths)}')
print(f'AoC [Day 01][Part 2] Solution 1: {p2_solution_1(depths)} | Solution 2: {p2_solution_2(depths)}')