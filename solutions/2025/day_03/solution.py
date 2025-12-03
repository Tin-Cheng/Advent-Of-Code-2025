# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 3
    def getJoltage(self, s: str, i: int, l: int) -> str:
        if l == 0:
            return ''
        if len(s) - i == l:
            return s[i:]
        n = max(s[i: len(s) - l + 1])
        return n + self.getJoltage(s, s.index(n, i) + 1, l - 1)
        
                

    @answer(17311)
    def part_1(self) -> int:
        ret = 0
        for line in self.input:
            print(line)
            n = self.getJoltage(line, 0, 2)
            print('a', n)
            ret += int(n)
        return ret

    @answer(171419245422055)
    def part_2(self) -> int:
        ret = 0
        for line in self.input:
            print(line)
            n = self.getJoltage(line, 0, 12)
            print('a', n)
            ret += int(n)
        return ret

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
