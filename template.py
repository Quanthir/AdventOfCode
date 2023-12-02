solution = """#!/usr/bin/env python3

class Solution:
    year = <year>
    day = <day>
    input: str
    data: list

    def __init__(self, folder="."):
        with open(f"{folder}/input.txt") as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = self.input.split("\n")

    def part1(self):
        return "Unknown"

    def part2(self):
        return "Unknown"


if __name__ == "__main__":
    s = Solution()
    print(f"AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}")
    print(f"AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}")
"""
