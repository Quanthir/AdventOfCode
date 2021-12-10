#!/usr/bin/env python3

import re
from collections import defaultdict

class Solution:
    year = 2020
    day = 7
    input: str
    data: list
    holdsgold = set()

    class Bag:
        bags = []
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()


    def prepare_data(self):
        self.data = self.input.split("\n")
        data = [[x for x in line.split(' bags contain ')]
                for line in self.data]

        self.contained_in = defaultdict(set)
        self.contains = defaultdict(list)
        for color, colors in data:
            for i, c in re.findall(r'(\d+) (.*?) bag', colors):
                self.contained_in[c].add(color)
                self.contains[color].append((int(i), c))

    def check(self, color):
        for c in self.contained_in[color]:
            self.holdsgold.add(c)
            self.check(c)

    def cost(self, color):
        total = 0
        for i, c in self.contains[color]:
            total += i
            total += i * self.cost(c)
        
        return total

    def part1(self):
        self.holdsgold = set()
        self.check('shiny gold')
        return len(self.holdsgold)


    def part2(self):
        return self.cost('shiny gold')


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
