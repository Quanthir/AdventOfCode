#!/usr/bin/env python3
import re


class Solution:
    year = 2023
    day = 3
    input: str
    data: list
    re = re.compile(r"\d+")

    def __init__(self, folder="."):
        with open(f"{folder}/input.txt") as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = self.input.strip().split("\n")

    def find_numbers(self, line):
        """Generator to find numbers on each line"""
        end = 0
        while m := self.re.search(line, end):
            start = max(m.start() - 1, 0)
            end = m.end() + 1
            yield start, min(end, len(line) - 1), int(m[0])

    def has_symbol(self, y, start, end, check):
        """Checks if the number has any symbols adjacent to it"""
        return [
            f"{x + start}-{ln}"
            for ln in [max(y - 1, 0), y, min(y + 1, len(self.data) - 1)]
            for x, char in enumerate(self.data[ln][start:end])
            if check(char)
        ]

    def part1(self):
        """Part 1 asks for sum of all numbers near any symbol except ``.``"""
        return sum(
            number
            for y, line in enumerate(self.data)
            for start, end, number in self.find_numbers(line)
            if any(self.has_symbol(y, start, end, lambda c: c not in "1234567890."))
        )

    def part2(self):
        """Part 2
        Find the 2 number adjacent to ``*`` and multiply them and give the sum
        """
        # Find the numbers with ``*`` near to them
        numbers = [
            (number, coord)
            for y, line in enumerate(self.data)
            for start, end, number in self.find_numbers(line)
            for coord in self.has_symbol(y, start, end, lambda c: c == "*")
        ]

        checked = []

        def append(c, number):
            checked.append(c)
            return number

        result = [
            append(c1, n1 * n2)
            for i, (n1, c1) in enumerate(numbers)
            for j, (n2, c2) in enumerate(numbers)
            if j != i and c1 == c2 and c1 not in checked
        ]

        return sum(result)


if __name__ == "__main__":
    s = Solution()
    print(f"AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}")
    print(f"AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}")
