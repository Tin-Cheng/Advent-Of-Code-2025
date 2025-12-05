# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/5

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 5

    @answer(525)
    def part_1(self) -> int:
        ret = 0
        fresh_ranges = []
        ingredients = []
        firstHalf = True
        for line in self.input:
            if line == '':
                firstHalf = False
                continue
            if firstHalf:
                r = line.split('-')
                fresh_ranges.append([int(r[0]),int(r[1])])
            else:
                ingredients.append(int(line))
        fresh_ranges.sort()
        ingredients.sort()
        i = 0
        for ig in ingredients:
            while i < len(fresh_ranges) and fresh_ranges[i][1] < ig :
                i += 1
            if i == len(fresh_ranges):
                break
            if fresh_ranges[i][0] <= ig and fresh_ranges[i][1] >= ig:
                ret += 1
        return ret

    @answer(333892124923577)
    def part_2(self) -> int:
        ret = 0
        fresh_ranges = []
        firstHalf = True
        for line in self.input:
            if line == '':
                firstHalf = False
                break
            if firstHalf:
                r = line.split('-')
                fresh_ranges.append([int(r[0]),int(r[1])])
        fresh_ranges.sort()
        final_ranges = []
        start, end = fresh_ranges[0][0], fresh_ranges[0][1] 
        for range in fresh_ranges:
            if range[0] > end:
                final_ranges.append([start,end])
                start, end = range[0], range[1]
            else:
                end = max(end,range[1])
        final_ranges.append([start,end])
        for range in final_ranges:
            ret += range[1] - range[0] + 1
        return ret

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
