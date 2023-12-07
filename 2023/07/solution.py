#!/usr/bin/env python3
import collections


class Solution:
    year = 2023
    day = 7
    input: str
    data: list

    def __init__(self, folder="."):
        with open(f"{folder}/input.txt") as f:
            self.input = f.read().strip()
        self.prepare_data()

    def prepare_data(self):
        self.data = [x.split() for x in self.input.split("\n")]

    def calculate(self, hand, is_part1):
        if is_part1:
            hand = hand.replace("J", "X")
        converted = ["J23456789TXQKA".index(x) + 1 for x in hand]
        strengths = [
            [
                (1, 1, 1, 1, 1),
                (1, 1, 1, 2),
                (1, 2, 2),
                (1, 1, 3),
                (2, 3),
                (1, 4),
                (5,),
            ].index(v)
            for c in "23456789TQKA"
            if (v := tuple(sorted(collections.Counter(hand.replace("J", c)).values())))
        ]
        return (max(strengths), *converted)

    def solve(self, is_part1):
        data = sorted(
            (self.calculate(hand, is_part1), int(bid)) for hand, bid in self.data
        )
        return sum(rank * bid for rank, (_, bid) in enumerate(data, start=1))

    def part1(self):
        return self.solve(True)

    def part2(self):
        return self.solve(False)


if __name__ == "__main__":
    s = Solution()
    print(f"AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}")
    print(f"AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}")
