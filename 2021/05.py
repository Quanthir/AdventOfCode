data = ""

with open('2021/05.txt') as f:
    data = f.read()

class Coord:
    start_x: int
    start_y: int
    end_x: int
    end_y: int

    def __init__(self, s: str):
        start, end = s.split(' -> ')
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))

        self.start_x = x1 if x1 < x2 else x2
        self.start_y = y1 if y1 < y2 else y2
        self.end_x = x1 if x1 > x2 else x2
        self.end_y = y1 if y1 > y2 else y2
    
    @property
    def is_horizontal(self) -> bool:
        return self.start_x != self.end_x
    
    @property
    def is_vertical(self) -> bool:
        return self.start_y != self.end_y
    
    @property
    def is_diagonal(self) -> bool:
        return abs(self.end_x - self.start_x) == abs(self.end_y - self.start_y)

class Matrix:
    m: list
    
    def __init__(self):
        self.m = []

    def expand(self, c: Coord):
        while len(self.m) <= c.end_y:
            self.m.append([])
        
        for y in range(c.start_y, c.end_y + 1):
            while len(self.m[y]) <= c.end_x:
                self.m[y].append(0)
    

data = [Coord(line) for line in data.split("\n")]

def solution1(data: list):
    matrix = Matrix()

    for c in data:
        if c.is_horizontal:
            matrix.expand(c)
            for x in range(c.start_x, c.end_x + 1):
                matrix.m[c.start_y][x] += 1
        elif c.is_vertical:
            matrix.expand(c)
            for y in range(c.start_y, c.end_y + 1):
                matrix.m[y][c.start_x] += 1
    
    return sum(1 for y in matrix.m for x in y if x > 1)


print(f'AoC [Day 05][Part 1] Solution: {solution1(data)}')
