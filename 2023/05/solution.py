#!/usr/bin/env python3


class Map:
    def __init__(self, data):
        self.data = [tuple(map(int, line.split())) for line in data.split("\n")[1:]]

    def part1(self, seed):
        for dest, src, rng in self.data:
            if src <= seed < src + rng:
                return seed + dest - src
        return seed

    def part2(self, seeds):
        result = []
        for dest, src, sz in self.data:
            src_end = src + sz
            ranges = []
            while seeds:
                (st, end) = seeds.pop()
                before = (st, min(end, src))
                inter = (max(st, src), min(src_end, end))
                after = (max(src_end, st), end)
                if before[1] > before[0]:
                    ranges.append(before)
                if inter[1] > inter[0]:
                    result.append((inter[0] - src + dest, inter[1] - src + dest))
                if after[1] > after[0]:
                    ranges.append(after)
            seeds = ranges
        return result + seeds


class Solution:
    year = 2023
    day = 5
    input: str
    data: list

    def __init__(self, folder="."):
        with open(f"{folder}/input.txt") as f:
            self.input = f.read().strip()
        self.prepare_data()

    def prepare_data(self):
        data = self.input.split("\n\n")
        self.seeds = [int(x) for x in data.pop(0)[7:].split(" ")]
        self.maps = [Map(m) for m in data]

    def part1(self):
        results = []
        for seed in self.seeds:
            for m in self.maps:
                seed = m.part1(seed)
            results.append(seed)
        return min(results)

    def part2(self):
        results = []
        seeds = list(zip(self.seeds[::2], self.seeds[1::2]))
        for st, sz in seeds:
            res = [(st, st + sz)]
            for m in self.maps:
                res = m.part2(res)
            results.append(min(res)[0])

        return min(results)


if __name__ == "__main__":
    s = Solution()
    print(f"AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}")
    print(f"AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}")
