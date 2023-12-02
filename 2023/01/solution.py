#!/usr/bin/env python3
import re


class Solution:
    year = 2023
    day = 1
    input: str
    data: list

    def __init__(self, folder="."):
        with open(f"{folder}/input.txt") as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = self.input.split("\n")

    def extract_calibration(self, line):
        # Remove everything except digits
        number = re.sub(r"\D", "", line)
        # There might be no number in the line at all
        first_number = number[0] if len(number) > 0 else "0"
        # If there is only one number in the line, double it. 6 becomes 66
        last_number = number[-1] if len(number) > 1 else first_number

        return int(f"{first_number}{last_number}")

    def part1(self):
        result = sum([self.extract_calibration(line) for line in self.data])
        return result

    def part2(self):
        result = 0

        for raw in self.data:
            line = raw
            # End of a string might be start of other string to correctly
            # convert all this is the easiest method.
            for old, new in [
                ("one", "o1e"),
                ("two", "t2o"),
                ("three", "t3e"),
                ("four", "f4r"),
                ("five", "f5e"),
                ("six", "s6x"),
                ("seven", "s7n"),
                ("eight", "e8t"),
                ("nine", "n9e"),
            ]:
                line = line.replace(old, new)
            result += self.extract_calibration(line)

        return result


if __name__ == "__main__":
    s = Solution()
    print(f"AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}")
    print(f"AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}")
