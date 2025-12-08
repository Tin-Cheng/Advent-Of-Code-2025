# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/8

from ...base import StrSplitSolution, answer
from collections import defaultdict
import math


class Solution(StrSplitSolution):
    _year = 2025
    _day = 8

    def getDistance(self, a: str, b: str) -> int:
        x1, y1, z1 = map(int, a.split(","))
        x2, y2, z2 = map(int, b.split(","))
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    
    def getParent(self, parents: list[int], a: int) -> int:
        if parents[a] != a:
            parents[a] = self.getParent(parents, parents[a])
        return parents[a]

    @answer(123420)
    def part_1(self) -> int:
        runs = 10 if self.use_test_data else 1000
        distance = []
        for i in range(len(self.input) - 1):
            for j in range(i + 1, len(self.input)):
                distance.append(
                    [self.getDistance(self.input[i], self.input[j]), i, j]
                )
        distance.sort()
        groups = [i for i in range(len(self.input))]
        for i in range(runs):
            d, a, b = distance[i]
            groups_a = self.getParent(groups, a)
            groups_b = self.getParent(groups, b)
            if groups_a != groups_b:
                groups[groups_b] = groups_a
        count = [0] * len(self.input)
        for i in range(len(groups)):
            parent = self.getParent(groups, i)
            count[parent] += 1
        count.sort()
        return count[-1] * count[-2] * count[-3]
        
        

    @answer(673096646)
    def part_2(self) -> int:
        distance = []
        for i in range(len(self.input) - 1):
            for j in range(i + 1, len(self.input)):
                distance.append(
                    [self.getDistance(self.input[i], self.input[j]), i, j]
                )
        distance.sort()
        remaining = len(self.input)
        groups = [i for i in range(len(self.input))]
        for i in range(len(distance)):
            d, a, b = distance[i]
            groups_a = self.getParent(groups, a)
            groups_b = self.getParent(groups, b)
            if groups_a != groups_b:
                groups[groups_b] = groups_a
                remaining -= 1
                if remaining == 1:
                    return int(self.input[a].split(",")[0]) * int(self.input[b].split(",")[0])
        return -1
        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
