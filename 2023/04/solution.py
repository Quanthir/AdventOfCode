#!/usr/bin/env python3
import re


class Solution:
    year = 2023
    day = 4
    input: str
    data: list

    def __init__(self, folder="."):
        with open(f"{folder}/input.txt") as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = [
            len(
                [
                    1
                    for _ in set(map(lambda x: int(x), left.split()))
                    & set(map(lambda x: int(x), right.split()))
                ]
            )
            for line in self.input.strip().split("\n")
            for left, right in [re.sub(r"Card +\d+: ", "", line).split(" | ")]
        ]

    def part1(self):
        return sum(
            2 ** (count - 1)
            for count in self.data
            if count > 0
        )

    def part2(self):
        result = [1] * len(self.data)
        generator = (
            (j, result[i])
            for i, count in enumerate(self.data)
            if count > 0
            for j in range(i + 1, i + 1 + count)
        )
        for i, copies in generator:
            result[i] += copies

        return sum(result)


if __name__ == "__main__":
    s = Solution()
    print(f"AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}")
    print(f"AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}")
