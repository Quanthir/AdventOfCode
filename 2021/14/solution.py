#!/usr/bin/env python3

from collections import Counter
from pprint import pprint


class Solution:
    year = 2021
    day = 14
    input: str
    data: list
    insertion: list
    
    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.insertion, data = self.input.split("\n\n")
        self.data = {x: y for line in data.split("\n") for x, y in [line.split(' -> ')]}
    
    def solution(self, steps: int) -> int:
        count = {x: Counter(x) for x in self.data.keys()}

        for _ in range(steps):
            new = dict()
            for key, insert in self.data.items():
                a, b = key
                c = count[a+insert] + count[insert+b]
                c[insert] -= 1
                new[key] = c
            count = new

        c = Counter()
        for a, b in zip(self.insertion, self.insertion[1:]):
            c += count[self.insertion[a+b]]
        c -= Counter(self.insertion[1:-1])

        most = c.most_common()[0]
        least = c.most_common()[-1]

        return most[1] - least[1]

    def part1(self):
        return self.solution(10)

    def part2(self):
        return self.solution(40)

    def test(self):
        temp = 'NNCB'
        rules = {
            'CH': 'B',
            'HH': 'N',
            'CB': 'H',
            'NH': 'C',
            'HB': 'C',
            'HC': 'B',
            'HN': 'C',
            'NN': 'C',
            'BH': 'H',
            'NC': 'B',
            'NB': 'B',
            'BN': 'B',
            'BB': 'N',
            'BC': 'B',
            'CC': 'N',
            'CN': 'C',
        }
        count = {x: Counter(x) for x in rules.keys()}

        for _ in range(10):
            new = dict()
            for key, i in rules.items():
                a, b = key
                c = count[a+i] + count[i+b]
                c[i] -= 1
                new[key] = c
            count = new
        
        c = Counter()
        for a, b in zip(temp, temp[1:]):
            c += count[a+b]
        c -= Counter(temp[1:-1])


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
