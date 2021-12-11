#!/usr/bin/env python3

class Solution:
    year = 2021
    day = 11
    input: str
    data: dict

    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        self.data = {
            (x, y): int(octopus)
            for y, line in enumerate(self.input.split("\n"))
                for x, octopus in enumerate(line) 
        }
    
    def test(self):
        """Prints the current data as 2D list.
        """
        test = ""
        for y in range(10):
            for x in range(10):
                test += str(self.data[(x,y)])
            test += "\n"
        print(test)

    def flash(self, x, y):
        self.data[(x, y)] = -1
        flashes = 1
        for c in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
            if c in self.data:
                if self.data[c] == -1:
                    continue
                if self.data[c] < 9:
                    self.data[c] += 1
                flashes += self.check(*c)
        
        return flashes


    def check(self, x, y):
        if self.data[(x, y)] == 9:
            self.data[(x, y)] = -1
            return self.flash(x, y)
        return 0
    
    def step(self, flashes):
        # Check for flashes
        for x, y in self.data.keys():
            flashes += self.check(x, y)

        # increase by one for the round
        for key in self.data.keys():
            self.data[key] += 1

    def part1(self):
        flashes = 0
        for _ in range(100): # for 100 steps
            flashes = self.step(flashes)
        
        return flashes

    def part2(self):
        self.prepare_data()
        step = 0
        while True:
            step += 1
            self.step(0)

            if all(x == 0 for x in self.data.values()):
                return step



if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
