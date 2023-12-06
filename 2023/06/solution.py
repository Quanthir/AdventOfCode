#!/usr/bin/env python3
import math


class Solution:
    year = 2023
    day = 6
    input: str
    data: list

    def __init__(self, folder="."):
        with open(f"{folder}/input.txt") as f:
            self.input = f.read().strip()
        self.prepare_data()

    def prepare_data(self):
        self.time, self.distance = [
            list(map(int, line[9:].split())) for line in self.input.split("\n")
        ]

    def find_wins(self, time, distance):
        return len([1 for hold in range(time) if hold * (time - hold) > distance])

    def part1(self):
        return math.prod(
            [
                self.find_wins(time, distance)
                for time, distance in zip(self.time, self.distance)
            ]
        )

    def part2(self):
        time, distance = (
            int("".join(map(str, self.time))),
            int("".join(map(str, self.distance))),
        )
        return self.find_wins(time, distance)


if __name__ == "__main__":
    s = Solution()
    print(f"AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}")
    print(f"AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}")
