#!/usr/bin/env python3

from pprint import pprint
from typing import ChainMap


class Solution:
    year = 2020
    day = 11
    input: str
    data: list
    
    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = self.input.split("\n")
    
    def adjacents(self, data, x, y):
        adj = []
        for dx in (x-1,x,x+1):
            for dy in (y-1,y,y+1):
                if (dx, dy) == (x, y):
                    continue
                if 0 <= dx < len(data) and 0 <= dy < len(data[0]):
                    adj.append(data[dx][dy])
        return adj

    def round(self, data):
        grid = ['' for _ in range(len(data))]
        changed = False
        for x, row in enumerate(data):
            for y, v in enumerate(row):
                if v == '.':
                    grid[x] += '.'
                    continue
                
                adj = ''.join(self.adjacents(data, x, y))
                if v == 'L':
                    if adj.count('#') == 0:
                        grid[x] += '#'
                        changed = True
                    else:
                        grid[x] += 'L'
                elif v == '#':
                    if adj.count('#') >= 4:
                        grid[x] += 'L'
                        changed = True
                    else:
                        grid[x] += '#'
        return changed, grid

    def part1(self):
        grid = self.data
        changed = True
        while changed:
            changed, grid = self.round(grid)

        return ''.join(grid).count('#')

    def part2(self):
        pass


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
