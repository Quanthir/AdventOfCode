#!/usr/bin/env python

class Solution:
    year = 2021
    day = 7
    input: str
    data: list

    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()


    def prepare_data(self):
        self.data = [*map(int, self.input.split(","))]


    def part1(self):
        return min([sum([abs(targetPos - crab) for crab in self.data]) for targetPos in range(max(*self.data))])


    def part2(self):
        f = lambda n: n * (n + 1) // 2
        return min([sum([f(abs(targetPos - crab)) for crab in self.data]) for targetPos in range(max(*self.data))])


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
