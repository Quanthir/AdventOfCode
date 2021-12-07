#!/usr/bin/env python

class Solution:
    year = 2021
    day = 1
    input: str
    data: list
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()


    def prepare_data(self):
        self.data = [*map(int, self.input.split("\n"))]


    def part1(self, data=None):
        if data is None:
            data = self.data
        return sum(data[i + 1] > data[i] for i in range(len(data) - 1))


    def part2(self):
        chunk = [a + b + c for a, b, c in zip(self.data, self.data[1::], self.data[2::])]
        return self.part1(chunk)


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
