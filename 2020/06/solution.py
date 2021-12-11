#!/usr/bin/env python3

class Solution:
    year = 2020
    day = 6
    input: str
    data: list

    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = self.input.split("\n\n")

    def part1(self):
        data = [x.replace("\n", "") for x in self.data]
        return sum(len(set(list(group))) for group in data)

    def part2(self):
        data = [
            [
                set(person)
                for person in group.split("\n")
            ]
            for group in self.data
        ]
        
        return sum(len(set.intersection(*group)) for group in data)


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
