# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/7

from ...base import StrSplitSolution, answer
from collections import defaultdict


class Solution(StrSplitSolution):
    _year = 2025
    _day = 7

    @answer(1628)
    def part_1(self) -> int:
        current_line = set()
        current_line.add(self.input[0].index('S'))
        intersactions = set()
        count = 0
        for y, line in enumerate(self.input):
            next_line = set()
            for x in current_line:
                if x < 0 or x >= len(line):
                    continue
                if line[x] == '^':
                    next_line.add(x - 1)
                    next_line.add(x + 1)
                    intersactions.add((x, y))
                    count += 1
                else:
                    next_line.add(x)
            current_line = next_line
        return len(intersactions)

    # @answer(1234)
    def part_2(self) -> int:
        current_line = set()
        S = self.input[0].index('S')
        current_line.add(S)
        intersactions = defaultdict(int)
        intersactions[(S, 0)] = 1
        count = 0
        for y, line in enumerate(self.input):
            if y == 0:
                continue
            next_line = set()
            for x in current_line:
                if x < 0 or x >= len(line):
                    continue
                if line[x] == '^':
                    next_line.add(x - 1)
                    next_line.add(x + 1)
                    intersactions[(x - 1, y)] += intersactions[(x, y - 1)]
                    intersactions[(x + 1, y)] += intersactions[(x, y - 1)]
                else:
                    next_line.add(x)
                    intersactions[(x, y)] += intersactions[(x, y - 1)]
            current_line = next_line
        for k in intersactions.keys():
            if k[1] == len(self.input) - 1:
                count += intersactions[k]
        return count

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
