#!/usr/bin/env python3

from collections import namedtuple

Inst = namedtuple('Inst', ['Cmd', 'Val'])

class Solution:
    year = 2020
    day = 8
    input: str
    data: list
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()


    def prepare_data(self):
        self.data = [{'c': line[:3], 'v': int(line[4:])} for line in self.input.split("\n")]


    def part1(self):
        visited = []
        acc = 0
        i = 0
        while i < len(self.data):
            if i in visited:
                break

            visited.append(i)

            if self.data[i]['c'] == 'acc':
                acc += self.data[i]['v']
            
            if self.data[i]['c'] == 'jmp':
                i += self.data[i]['v']
            else:
                i += 1
        
        return acc


    def part2(self):
        pass


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
