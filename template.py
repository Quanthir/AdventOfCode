solution = """
#!/usr/bin/env python

class Solution:
    input: str
    year = <year>
    day = <day>
    
    def __init__(self):
        with open('./input.txt') as f:
            self.input = f.read()
        
        self.prepare_data()
    
    def prepare_data(self):
        pass

    def part1(self):
        pass

    def part2(self):
        pass

if __name__ == '__main__':
    s = Solution()
    print(f'AoC [{s.year} - Day {s.day}] Part 1: {s.part1}')
    print(f'AoC [{s.year} - Day {s.day}] Part 2: {s.part2}')
"""
