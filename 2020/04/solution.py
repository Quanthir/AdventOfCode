#!/usr/bin/env python3

import re


class Solution:
    year = 2020
    day = 4
    input: str
    data: list
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()


    def prepare_data(self):
        self.data = [x.replace("\n", " ") for x in self.input.split("\n\n")]


    def part1(self):
        valids = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        return sum(all(x in p for x in valids) for p in self.data)


    def part2(self):
        tests = [
            r'byr:(19[2-9]\d|200[0-2])',
            r'iyr:(201\d|2020)',
            r'eyr:(202\d|2030)',
            r'hgt:(1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in)',
            r'hcl:\#[0-9a-f]{6}',
            r'ecl:(amb|blu|brn|gry|grn|hzl|oth)',
            r'pid:\d{9}(?!\d)',
        ]

        return sum(all(re.search(r, passport) for r in tests) for passport in self.data)


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
