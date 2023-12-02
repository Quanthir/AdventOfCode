#!/usr/bin/env python3
import numpy


class Solution:
    year = 2023
    day = 2
    input: str
    data: list

    def __init__(self, folder="."):
        with open(f"{folder}/input.txt") as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = [line.split(": ") for line in self.input.split("\n") if line]
        # Convert list to following format:
        # { id: [[(1, 'red'), (2, 'blue')]] }
        self.data = {
            int(game.replace("Game ", "")): [
                [
                    (int(cube.split(" ")[0]), cube.split(" ")[1])
                    for cube in game_set.split(", ")
                ]
                for game_set in data.split("; ")
            ]
            for game, data in self.data
        }

    valid_counts = {"red": 12, "green": 13, "blue": 14}

    def is_valid(self, sets):
        for set in sets:
            data = {color: 0 for _, color in set}
            for count, color in set:
                data[color] += count
                if data[color] > self.valid_counts[color]:
                    return False
        return True

    def part1(self):
        generator = (id for id, sets in self.data.items() if self.is_valid(sets))
        return sum([id for id in generator])

    def part2(self):
        result = []
        for sets in self.data.values():
            cubes = {}
            entries = [cube for set in sets for cube in set]
            generator = (
                (count, color)
                for count, color in entries
                if color not in cubes or cubes[color] < count
            )
            for count, color in generator:
                cubes[color] = count

            result.append(numpy.prod([cube for cube in cubes.values()]))

        return sum(result)


if __name__ == "__main__":
    s = Solution()
    print(f"AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}")
    print(f"AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}")
