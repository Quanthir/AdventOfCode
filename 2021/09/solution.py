#!/usr/bin/env python3

class Solution:
    year = 2021
    day = 9
    input: str
    data: list
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        self.prepare_data()


    def prepare_data(self):
        self.data = self.input.split("\n")
        self.data = {(y, x): int(self.data[y][x]) for y in range(len(self.data)) for x in range(len(self.data[y]))}


    def part1(self):
        lowp = []
        for c, x in self.data.items():
            print(c[0], c[1], x)
        # for y in range(len(self.data)):
        #     for x in range(len(self.data[y])):
        #         adj = []
        #         if y > 0:
        #             adj.append(self.data[y - 1][x])
        #         if x > 0:
        #             adj.append(self.data[y][x - 1])
        #         if y < len(self.data) - 1:
        #             adj.append(self.data[y + 1][x])
        #         if x < len(self.data[y]) - 1:
        #             adj.append(self.data[y][x + 1])
                
        #         if self.data[y][x] < min(adj):
        #             lowp.append(self.data[y][x] + 1)

        return sum(lowp)


    def countFlow(self, y, x, checked = []):
        low = self.data[y][x] - 1
        high = self.data[y][x] + 1

    def part2(self):
        pass


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
