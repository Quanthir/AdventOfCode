#!/usr/bin/env python3

class Solution:
    year = 2020
    day = 9
    input: str
    data: list
    
    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = list(map(int, self.input.split("\n")))

    def part1(self):
        for i in range(25, len(self.data)):
            preamble = self.data[i-25:i]
            sums = [x + y for x in preamble for y in preamble if x + y == self.data[i]]

            if len(sums) == 0:
                return self.data[i]

    def part2(self):
        target = self.part1()

        for i in range(len(self.data)):
            numbers = []
            s = i
            while sum(numbers) < target:
                numbers.append(self.data[s])
                s += 1
            
            if sum(numbers) == target:
                numbers.sort()
                return numbers[0] + numbers[-1]



if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
