#!/usr/bin/env python3


class Solution:
    year = 2021
    day = 12
    input: str
    data: list
    exits: dict
    
    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = {}
        for line in self.input.split("\n"):
            source, dest = line.split('-')
            self.data.setdefault(source, set())
            self.data.setdefault(dest, set())
            self.data[source].add(dest)
            self.data[dest].add(source)
    
    def count(self, room='start', visited={'start'}, double=False):
        if room == 'end':
            return 1
        
        count = 0
        for r in self.data[room]:
            if r.isupper():
                count += self.count(r, visited, double)
            elif r not in visited:
                count += self.count(r, visited | {r}, double)
            elif double and r != 'start':
                count += self.count(r, visited, False)
        
        return count

    def part1(self):
        return self.count()

    def part2(self):
        return self.count(double=True)


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
