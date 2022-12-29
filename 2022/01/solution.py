#!/usr/bin/env python3


class Solution:
    year = 2022
    day = 1
    input: str
    data: list

    def __init__(self, folder="."):
        with open(f"{folder}/input.txt") as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.input = self.input.split("\n\n")

    def part1(self):
        self.elfs = []
        for bucket in self.input:
            points = [int(x) for x in bucket.split("\n")]
            self.elfs.append(sum(points))

        return max(self.elfs)

    def part2(self):
        return sum(sorted(self.elfs, reverse=True)[:3])


if __name__ == "__main__":
    s = Solution()
    print(f"AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}")
    print(f"AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}")
