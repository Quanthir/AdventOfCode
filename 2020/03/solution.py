#!/usr/bin/env python3

from functools import reduce


class Solution:
    year = 2020
    day = 3
    input: str
    data: list
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = self.input.split("\n")

    def solution(self, right, down):
        x, y, count = 0, 0, 0
        while y < len(self.data) - 1:
            y += down
            x = (x + right) % len(self.data[y])

            if self.data[y][x] == '#':
                count += 1
        
        return count

    def part1(self):
        return self.solution(3, 1)

    def part2(self):
        pattern = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
        return reduce(lambda a, b: a * self.solution(*b), pattern, 1)


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
