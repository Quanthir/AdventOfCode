#!/usr/bin/env python3

class Solution:
    year = 2021
    day = 6
    input: str
    data: list
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()


    def prepare_data(self):
        self.data = [int(x) for x in self.input.split(',')]


    def solution(self, days: int) -> int:
        f = [*map(self.input.count, '012345678')]

        for _ in range(days):
            f = f[1:] + f[:1]
            f[6] += f[-1]

        return sum(f)


    def part1(self):
        return self.solution(80)


    def part2(self):
        return self.solution(256)


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
