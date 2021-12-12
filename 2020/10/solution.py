#!/usr/bin/env python3

from pprint import pprint


class Solution:
    year = 2020
    day = 10
    input: str
    data: list
    adapter: int

    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = list(map(int, self.input.split("\n")))
        self.data.sort()
        self.adapter = max(self.data) + 3

    def part1(self):
        zipped = list(zip(self.data, self.data[1:]))
        count1 = sum(1 for a, b in zipped if a + 1 == b) + 1
        count3 = sum(1 for a, b in zipped if a + 3 == b) + 1
        return count1 * count3
    
    def count(self, jolt=0):
        if self.adapter - 3 <= jolt <= self.adapter:
            return 1
        
        count = 0
        if jolt + 1 in self.data:
            count += self.count(jolt + 1)
        if jolt + 2 in self.data:
            count += self.count(jolt + 2)
        if jolt + 3 in self.data:
            count += self.count(jolt + 3)
        
        return count

    def part2(self):
        jolt = 0
        print(jolt + 3 in self.data)
        pprint(self.data)
        # return self.count()


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
