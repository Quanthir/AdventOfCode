#!/usr/bin/env python3

import re

class Solution:
    year = 2020
    day = 2
    input: str
    data: list

    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        data = [re.match(r'(\d+)-(\d+) (\w): (\w+)', x).groups() for x in self.input.split("\n")]
        self.data = [[int(x[0]), int(x[1]), x[2], x[3]] for x in data]

    def part1(self):
        return sum(x[0] <= x[3].count(x[2]) <= x[1] for x in self.data)

    def part2(self):
        puz = lambda p1, p2, c, s: (s[p1] == c or s[p2] == c) and s[p1] != s[p2]
        return sum(puz(x[0]-1, x[1]-1, x[2], x[3]) for x in self.data)


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
