#!/usr/bin/env python3

from math import prod

class Solution:
    year = 2021
    day = 9
    input: str
    data: list
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()


    def prepare_data(self):
        self.data = {(x, y): int(d) for y, line in enumerate(self.input.split("\n"))
                                    for x, d in enumerate(line.strip())}


    def neighbours(self, x, y):
        return filter(lambda n: n in self.data, [(x, y-1), (x, y+1), (x-1,y), (x+1,y)])


    def is_low(self, key):
        return all(self.data[key] < self.data[n] for n in self.neighbours(*key))


    def part1(self):
        lowp = list(filter(self.is_low, self.data))
        return sum(self.data[key] + 1 for key in lowp)


    def count(self, key):
        if self.data[key] == 9: return 0
        del self.data[key]
        return 1 + sum(map(self.count, self.neighbours(*key)))


    def part2(self):
        lowp = list(filter(self.is_low, self.data))
        basins = [self.count(key) for key in lowp]
        return prod(sorted(basins)[-3:])


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
