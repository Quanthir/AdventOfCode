#!/usr/bin/env python3

class Solution:
    year = 2020
    day = 11
    input: str
    data: list
    
    def __init__(self, folder='.'):
        with open(f'{folder}/input.txt') as f:
            self.input = f.read()
        self.prepare_data()

    def prepare_data(self):
        # first we need to determine the grid max dimensions.
        grid = [[seat for seat in line] for line in self.input.split("\n")]
        # Then need to create a coordinate map (which will be our main data)
        # we will ignore the dots since they have no value for the puzzle
        self.data = {
            (x, y): 0
            for y, row in enumerate(grid)
                for x, seat in enumerate(row) if seat == 'L'
        }
    
    def neighbours(self, x, y):
        """ Gives the adjacent seat coordinates for the given coordinate
        """
        return [
            adj
            for adj in self.data.keys()
            if adj in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
        ]

    def part1(self):
        # We need to loop all coordinates and apply the given rules to each seat
        # depending of their situations.
        # this is just one round. We need to loop it until no changes occur
        changed = True
        while changed:
            changed = False
            for coord, seat in self.data.items():
                neighbours = self.neighbours(*coord)
                if seat == 0 and all(self.data[s] == 0 for s in neighbours):
                    # if all seats in neighbours is empty, make the seat occupied
                    self.data[coord] = 1
                    changed = True
                elif seat == 1 and sum(self.data[s] == 1 for s in neighbours) > 3:
                    # if 4 or more seats in neighbours occupied, empty it
                    self.data[coord] = 0
                    changed = True
        
        return sum(seat for seat in self.data.values() if seat == 1)

    def part2(self):
        pass


if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1()}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2()}')
