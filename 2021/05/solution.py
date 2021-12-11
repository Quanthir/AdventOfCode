#!/usr/bin/env python3

from  collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['Start', 'End'])

class Solution:
    year = 2021
    day = 5
    input: str
    data: list

    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        data = [
            [
                [int(x) for x in row.split(',')]
                for row in line.split(' -> ')
            ]
            for line in self.input.split("\n")
        ]
        self.data = [Line(Point(*row[0]), Point(*row[1])) for row in data]

    @staticmethod
    def generate_points(line: Line, horizontal = False) -> Point:
        if line.Start == line.End:
            yield line.Start
            return
        
        dx = abs(line.End.x - line.Start.x)
        dy = abs(line.End.y - line.Start.y)
        minx = min(line.Start.x, line.End.x)
        miny = min(line.Start.y, line.End.y)

        if not (dx != 0 and dy != 0):
            for i in range(minx, minx + dx + 1):
                for j in range(miny, miny + dy + 1):
                    yield Point(i, j)

        if horizontal and dx == dy:
            yield line.Start
            x = line.Start.x
            y = line.Start.y
            while x != line.End.x:
                if line.End.x > line.Start.x:
                    x += 1
                else:
                    x -= 1

                if line.End.y > line.Start.y:
                    y += 1
                else:
                    y -= 1

                yield Point(x, y)

    def solution(self, horizontal = False) -> int:
        matrix = {}
        count = 0
        for line in self.data:
            for point in self.generate_points(line, horizontal):
                matrix.setdefault(point, 0)

                matrix[point] += 1
                if matrix[point] == 2:
                    count += 1

        return count

    def part1(self):
        return self.solution(False)

    def part2(self):
        return self.solution(True)


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
