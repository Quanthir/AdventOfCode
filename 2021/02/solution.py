#!/usr/bin/env python3

class Solution:
    year = 2021
    day = 2
    input: str
    data: list

    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = [[x for x in line.split()] for line in self.input.split("\n")]

    def part1(self):
        height = 0
        depth = 0
        for x in self.data:
            if x[0] == 'forward':
                height += int(x[1])
            elif x[0] == 'up':
                depth -= int(x[1])
            else:
                depth += int(x[1])

        return height * depth

    def part2(self):
        height = 0
        aim = 0
        depth = 0

        for x in self.data:
            if x[0] == 'forward':
                height += int(x[1])
                depth += int(x[1]) * aim
            elif x[0] == 'up':
                aim -= int(x[1])
            else:
                aim += int(x[1])

        return height * depth


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
