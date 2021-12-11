#!/usr/bin/env python3

class Solution:
    year = 2021
    day = 4
    input: str
    drawn: list
    data: list

    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        data = self.input.split("\n\n")
        self.drawn = list(map(int, data[0].split(',')))
        self.data = [
            [
                [int(x) for x in map(str.strip, row.split(' ')) if x]
                for row in line.split("\n")
            ]
            for line in data[1:]
        ]

    def solution(self, part = 'part1'):
        seen, won, scores = [], [], []
        for n in self.drawn:
            seen.append(n)
            for board in self.data:
                transpose = list(zip(*board))
                for i, line in enumerate(board):
                    if (
                        all(num in seen for num in line)
                        or all(num in seen for num in transpose[i])
                    ) and board not in won:
                        won.append(board)
                        scores.append(
                            sum(
                                sum(num for num in line if num not in seen)
                                for line in board
                            )
                            * seen[-1]
                        )
        
        if part == 'part1':
            return scores[0]
        else:
            return scores[-1]

    def part1(self):
        return self.solution('part1')

    def part2(self):
        return self.solution('part2')


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
