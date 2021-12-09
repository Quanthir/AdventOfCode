#!/usr/bin/env python3

class Solution:
    year = 2021
    day = 3
    input: str
    data: list
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()


    def prepare_data(self):
        self.data = self.input.split("\n")


    def part1(self):
        high, low = '', ''

        for i in range(len(self.data[0])):
            c0, c1 = 0, 0
            for x in self.data:
                if x[i] == '0': c0 += 1
                else:           c1 += 1
            
            if c0 > c1:
                high += "0"
                low  += "1"
            else:
                high += "1"
                low  += "0"
        
        return int(high, 2) * int(low, 2)


    @classmethod
    def finder(cls, data, i, find):
        if len(data) == 1: return data

        p0, p1 = [], []
        for x in data:
            if x[i] == "0":
                p0.append(x)
            else:
                p1.append(x)

        if len(p0) == len(p1):
            return cls.finder(p1 if find == 'most' else p0, i + 1, find)

        if find == 'most':
            return cls.finder(p1 if len(p1) > len(p0) else p0, i + 1, find)
        else:
            return cls.finder(p0 if len(p0) < len(p1) else p1, i + 1, find)


    def part2(self):
        most = self.finder(self.data, 0, 'most')
        less = self.finder(self.data, 0, 'less')
        return int(most[0], 2) * int(less[0], 2)


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
