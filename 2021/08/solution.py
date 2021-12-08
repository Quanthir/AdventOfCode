#!/usr/bin/env python3

from collections import namedtuple

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
        self.data = [[[x for x in part.split(' ')] for part in line.split(" | ")] for line in self.input.split("\n")]


    def part1Cond(self, data: str) -> bool:
        if 2 <= len(data) <= 4 or len(data) == 7:
            return True


    def part1(self):
        inp = [x for row in self.data for x in row[1]]
        return sum([1 for x in inp if self.part1Cond(x)])


    def part2(self):
        
        pass


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
