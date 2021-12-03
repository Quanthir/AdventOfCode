import re

data = ""
with open("2020/day04.txt") as f:
    data = f.read().split("\n\n")

data = [x.replace("\n", " ") for x in data]

def solution1(data):
    valids = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    count = 0
    for passport in data:
        if all(x in passport for x in valids):
            count += 1
    
    return count
    # valids = 0
    # for x in data:
    #     pport = {v[0:3]:v[4::] for v in x}
    #     if len(pport) == 8 or len(pport) == 7 and pport.get('cid') == None:
    #         valids += 1

    # return valids


def solution2(data):
    tests = [
        r'byr:(19[2-9]\d|200[0-2])',
        r'iyr:(201\d|2020)',
        r'eyr:(202\d|2030)',
        r'hgt:(1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in)',
        r'hcl:#[0-9a-f]{6}',
        r'ecl:(amb|blu|brn|gry|grn|hzl|oth)',
        r'pid:\d{9}',
    ]

    count = 0
    for x in data:
        res = [re.search(y, x) != None for y in tests]
        if all(res) and len(res) == 7:
            count += 1

    return count


print(f'AoC [Day 04][Part 1] Solution: {solution1(data)}')
print(f'AoC [Day 04][Part 2] Solution: {solution2(data)}')
