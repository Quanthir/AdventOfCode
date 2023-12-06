#!/usr/bin/env python3


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

        self.maps = [
            [tuple(map(int, line.split())) for line in m.split("\n")[1:]] for m in data
        ]

    def part1(self):
        results = []
        for seed in self.seeds:
            for m in self.maps:
                for dest, src, rng in m:
                    if src <= seed <= src + rng:
                        seed = seed + dest - src
                        break
            results.append(seed)

        return min(results)

    def find_seed(self, m, seed_start, seed_range, seeds, is_last=False):
        for dest, src, rng in m:
            if src <= seed_start <= src + rng:
                diff = (seed_start + seed_range) - (src + rng)
                if diff > 0 and not is_last:
                    seeds.append((seed_start + dest - src, min(diff, rng)))
                    self.find_seed(m, seed_start + rng, diff, seeds)
                else:
                    seeds.append(
                        (seed_start + dest - src, seed_range)
                        if not is_last
                        else seed_start + dest - src
                    )
                break

    def part2(self):
        seeds = list(zip(self.seeds[::2], self.seeds[1::2]))
        last_i = len(self.maps) - 1
        for i, m in enumerate(self.maps):
            new_seeds = []
            for seed_start, seed_range in seeds:
                self.find_seed(m, seed_start, seed_range, new_seeds, i == last_i)

            seeds = new_seeds

        return min(seeds)


if __name__ == "__main__":
    s = Solution()
    print(f"AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}")
    print(f"AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}")
