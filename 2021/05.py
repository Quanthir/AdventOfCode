from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['Start', 'End'])

data = ""

with open('2021/05.txt') as f:
    data = f.read()

data = [
    [
        [int(x) for x in row.split(',')]
        for row in line.split(' -> ')
    ]
    for line in data.split("\n")
]

data = [Line(Point(*row[0]), Point(*row[1])) for row in data]

def generate_points(line: Line, horizontal=False) -> Point:
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

def solution1(horizontal = False) -> int:
    matrix = {}
    count = 0
    for line in data:
        for point in generate_points(line, horizontal):
            matrix.setdefault(point, 0)

            matrix[point] += 1
            if matrix[point] == 2:
                count += 1
    
    return count

print(f'AoC [Day 03][Part 1] Solution: {solution1(False)}')
print(f'AoC [Day 03][Part 2] Solution: {solution1(True)}')
