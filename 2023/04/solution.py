#!/usr/bin/env python3

class Solution:
    year = 2023
    day = 4
    input: str
    data: list

    def __init__(self, folder="."):
        with open(f"{folder}/input.txt") as f:
            self.input = f.read().strip().split("\n")
        self.prepare_data()

    def prepare_data(self):
        self.solution1 = 0
        self.solution2 = [1] * len(self.input)

        for i, line in enumerate(self.input):
            left, right = line[10:].split(" | ")

            if (count := len(set(left.split()) & set(right.split()))):
                self.solution1 += 2 ** (count - 1)

            for j in range(count):
                self.solution2[i + j + 1] += self.solution2[i]

    def part1(self):
        return self.solution1

    def part2(self):
        return sum(self.solution2)


if __name__ == "__main__":
    s = Solution()
    print(f"AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}")
    print(f"AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}")
