#!/usr/bin/env python3


class Solution:
    year = 2020
    day = 8
    input: str
    data: list

    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = [{'c': line[:3], 'v': int(line[4:])} for line in self.input.split("\n")]

    def part1(self):
        acc = 0
        line = 0
        visited = []
        while line < len(self.data):
            if line in visited:
                break

            visited.append(line)

            if self.data[line]['c'] == 'acc':
                acc += self.data[line]['v']
            
            if self.data[line]['c'] == 'jmp':
                line += self.data[line]['v']
            else:
                line += 1

        return acc

    def check(self, key, to):
        acc = 0
        line = 0
        visited = []
        while line < len(self.data):
            if line in visited:
                break

            visited.append(line)

            if line == key and to == 'nop':
                line += 1
                continue

            if self.data[line]['c'] == 'acc':
                acc += self.data[line]['v']

            if self.data[line]['c'] == 'jmp' or (line == key and to == 'jmp'):
                line += self.data[line]['v']
            else:
                line += 1

        if line >= len(self.data):
            return acc
        else:
            return 0

    def part2(self):
        jmps = [line for line, v in enumerate(self.data) if v['c'] == 'jmp']
        nops = [line for line, v in enumerate(self.data) if v['c'] == 'nop']

        for line in jmps:
            acc = self.check(line, 'nop')
            if acc > 0:
                return acc
        
        for line in nops:
            acc = self.check(line, 'jmp')
            if acc > 0:
                return acc
        
        return 'Not Found!'



if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
