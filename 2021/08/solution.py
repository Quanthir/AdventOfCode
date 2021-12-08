#!/usr/bin/env python3

class Solution:
    year = 2021
    day = 8
    input: str
    data: list
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()


    def prepare_data(self):
        self.data = [
            [
                [
                    {c for c in word} for word in column.split(' ')
                ]
                for column in line.split(' | ')
            ]
            for line in self.input.split("\n")
        ]


    def part1Cond(self, data: str) -> bool:
        if 2 <= len(data) <= 4 or len(data) == 7:
            return True


    def part1(self):
        inp = [x for row in self.data for x in row[1]]
        return sum([1 for x in inp if self.part1Cond(x)])


    def part2Cond(self, data, i):
        return {ch for ch in list(x for x in data if len(x) == i)[0]}


    def part2(self):
        summ = 0
        for row in self.data:
            one = self.part2Cond(row[0], 2)
            four = self.part2Cond(row[0], 4)
            seven = self.part2Cond(row[0], 3)
            eight = self.part2Cond(row[0], 7)
            four_seven = set.union(four, seven)
            nine = {x for s in row[0] for x in s if len(s) == 6 and four_seven.issubset(s)}
            
            merged = ''.join([x for s in row[0] for x in s])

            u = next(x for x in seven if x not in one)
            d = list(set(nine) - four_seven)[0]
            ld = next(x for x in merged if merged.count(x) == 4)
            lu = next(x for x in merged if merged.count(x) == 6)
            rd = next(x for x in merged if merged.count(x) == 9)
            m  = next(x for x in merged if merged.count(x) == 7 and x != d)
            ru = next(x for x in merged if merged.count(x) == 8 and x != u)

            zero = {u, d, lu, ru, ld, rd}
            two = {u, ru, m, ld, d}
            three = {u, m, d, ru, rd}
            five = {u, m, d, lu, rd}
            six = {u, m, d, lu, ld, rd}
            numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

            n = ''
            for x in row[1]:
                n += next(str(i) for i in range(10) if numbers[i] == set(list(x)))
            
            summ += int(n)
        
        return summ


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
