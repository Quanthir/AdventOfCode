#!/usr/bin/env python3

from pprint import pprint


class Solution:
    year = 2020
    day = 10
    input: str
    data: list
    adapter: int

    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = sorted(list(map(int, self.input.split("\n"))))
        self.adapter = max(self.data) + 3

    def part1(self):
        zipped = list(zip(self.data, self.data[1:]))
        count1 = sum(1 for a, b in zipped if a + 1 == b) + 1 # plus one is for 0 outage
        count3 = sum(1 for a, b in zipped if a + 3 == b) + 1 # plus one is for +3 device adapter
        return count1 * count3
    
    def count(self, jolt = 0):
        """
        This brute force works but it takes quite time to find the
        solution (it takes nearly a hour!) because result is like 130 trillion
        So not a satisfactory solution.
        """
        if jolt == self.adapter:
            return 1
        
        count = 0
        for i in [1, 2, 3]:
            if jolt + i in self.data:
                count += self.count(jolt + i)
        
        return count

    def part2(self):
        self.data.append(self.adapter)
        # this solution takes alot of time to solve.
        # return self.count()
        # after some research, I came up with this solution.
        combinations = {0: 1}
        get = lambda jolt: combinations.get(jolt, 0)
        for jolt in self.data:
            combinations[jolt] = get(jolt-1) + get(jolt-2) + get(jolt-3)
        
        return combinations[max(combinations.keys())]


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
