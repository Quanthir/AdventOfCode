#!/usr/bin/env python3


class Solution:
    year = 2021
    day = 13
    input: str
    data: list
    
    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        data, folds = self.input.split("\n\n")
        self.data = [(int(x), int(y)) for line in data.split("\n") for x,y in [line.split(',')]]
        self.folds = [(k.replace('fold along ', ''), int(v)) for line in folds.split('\n') for k,v in [line.split('=')]]

    def fold(self, data, dim, val):
        fdim = 0 if dim == 'x' else 1
        first = {x for x in data if x[fdim] < val}
        def calc(x, y): return (x - (x - val) * 2, y) if dim == 'x' else (x, y - (y - val) * 2)
        will_fold = {calc(*x) for x in data if x[fdim] > val}
        return first | will_fold

    def part1(self):
        return len(self.fold(self.data, *self.folds[0]))

    def part2(self):
        self.prepare_data()
        data = self.data
        for fold in self.folds:
            data = self.fold(data, *fold)
        
        max_y = max(y for _, y in data) + 1
        max_x = max(x for x, _ in data) + 1
        paper = ['' for _ in range(max_y)]
        for y in range(max_y):
            for x in range(max_x):
                paper[y] += '#' if (x, y) in data else '.'
        
        for line in paper:
            print(line)
        return 'The text above!'


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
