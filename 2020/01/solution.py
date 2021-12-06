#!/usr/bin/env python

class Solution:
    input: str
    year = 2020
    day = 1
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        
        self.prepare_data()
    
    def prepare_data(self):
        self.input = [*map(int, self.input.split("\n"))]

    def part1(self):
        for x in self.input:
            for y in self.input:
                if x + y == 2020:
                    return x * y

    def part2(self):
        for x in self.input:
            for y in self.input:
                for z in self.input:
                    if x + y + z == 2020:
                        return x * y * z

if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
