data = ""
with open("2021/03.txt") as f:
    data = f.read().split("\n")

def solution1(data):
    high = ""
    low = ""

    for i in range(len(data[0])):
        c0, c1 = 0, 0
        for x in data:
            if x[i] == "0":
                c0 += 1
            else:
                c1 += 1
        
        if c0 > c1:
            high += "0"
            low += "1"
        else:
            high += "1"
            low += "0"
    
    return int(high, 2) * int(low, 2)

def finder(data, i, find):
    if len(data) == 1:
        return data

    p0, p1 = [], []
    for x in data:
        if x[i] == "0":
            p0.append(x)
        else:
            p1.append(x)
    
    if len(p0) == len(p1):
        return finder(p1 if find == 'most' else p0, i + 1, find)

    if find == 'most':
        return finder(p1 if len(p1) > len(p0) else p0, i + 1, find)
    else:
        return finder(p0 if len(p0) < len(p1) else p1, i + 1, find)

def solution2(data):
    most = finder(data, 0, 'most')
    less = finder(data, 0, 'less')
    
    print(most[0], less[0])
    return int(most[0], 2) * int(less[0], 2)
    


print(f'AoC [Day 03][Part 1] Solution: {solution1(data)}')
print(f'AoC [Day 03][Part 2] Solution: {solution2(data)}')
