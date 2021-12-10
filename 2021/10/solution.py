#!/usr/bin/env python3

import math
from functools import reduce

class Solution:
    year = 2021
    day = 10
    input: str
    data: list
    OPENINGS = {'(': ')','[': ']','{': '}','<': '>'}
    CLOSINGS = {')': '(', ']': '[', '}': '{', '>': '<'}
    P1_POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
    P2_POINTS = {')': 1, ']': 2, '}': 3, '>': 4}


    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()


    def prepare_data(self):
        self.data = self.input.split("\n")


    def interpret(self):
        errors = {')': 0, ']': 0, '}': 0, '>': 0}
        openings = []
        for line in self.data:
            opened = []
            notBroken = True
            for x in line:
                if x in self.OPENINGS:
                    opened.append(x)
                elif self.CLOSINGS[x] != opened[-1]:
                    errors[x] += 1
                    notBroken = False
                    break
                else:
                    opened.pop()
            
            if notBroken and len(opened) > 0:
                openings.append(opened)
        
        return errors, openings


    def part1(self):
        errors, _ = self.interpret()
        return sum(v * self.P1_POINTS[k] for k, v in errors.items())


    def part2(self):
        _, openings = self.interpret()
        scores = [
            reduce(lambda s, x: s * 5 + self.P2_POINTS[self.OPENINGS[x]], reversed(opened), 0)
            for opened in openings
        ]
        scores.sort()
        return scores[math.floor(len(scores) / 2)]


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
