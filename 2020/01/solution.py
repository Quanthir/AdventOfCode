#!/usr/bin/env python3

class Solution:
    year = 2020
    day = 1
    input: str
    data: list
    
    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = [int(x) for x in self.input.split("\n")]

    def part1(self):
        return next(x * y for x in self.data for y in self.data if x + y == 2020)

    def part2(self):
        return next(
            x * y * z
            for x in self.data for y in self.data for z in self.data
            if x + y + z == 2020
        )


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
