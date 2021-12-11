#!/usr/bin/env python3

class Solution:
    year = 2020
    day = 5
    input: str
    data: list

    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = [[line[:7], line[-3:]] for line in self.input.split("\n")]

    def solution(self):
        ids = []
        for line in self.data:
            rows = [i for i in range(128)]
            for x in line[0]:
                if x == 'F':
                    rows = rows[:len(rows)//2]
                else:
                    rows = rows[len(rows)//2:]

            cols = [i for i in range(8)]
            for x in line[1]:
                if x == 'L':
                    cols = cols[:len(cols)//2]
                else:
                    cols = cols[len(cols)//2:]

            ids.append(rows[0] * 8 + cols[0])
        
        return ids

    def part1(self):
        return max(self.solution())

    def part2(self):
        ids = self.solution()
        ids.sort()
        before = ids[0] - 1
        for seat in ids:
            if seat - before != 1:
               break
            before = seat
        
        return before + 1


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
