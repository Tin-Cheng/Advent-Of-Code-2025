# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/6

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 6

    @answer(3261038365331)
    def part_1(self) -> int:
        arr = []
        for line in self.input:
            arr.append(list(filter(lambda s: s != '', line.split(' '))))
        ret = 0
        for i in range(len(arr[0])):
            s = arr[-1][i]
            x = 1 if s == '*' else 0
            for j in range(len(arr)-2, -1, -1):
                if s == '*':
                    x *= int(arr[j][i])
                else:
                    x += int(arr[j][i])
            ret += x
        return ret
        

    @answer(8342588849093)
    def part_2(self) -> int:
        i = 0
        ret = 0
        while i < len(self.input[0]) - 1:
            s = self.input[-1][i]
            j = i + 1
            x = 1 if s == '*' else 0
            while j < len(self.input[0]) - 1 and self.input[-1][j] == ' ':
                j += 1
            nexti = j
            if self.input[-1][j] != ' ':
                j -= 1
            while j >= i:
                num = 0
                for k in range(len(self.input)-1):
                    if self.input[k][j] != ' ':
                        num = num * 10 + int(self.input[k][j])
                x = x * num if s == '*' and num > 0 else x + num
                j -= 1
            ret += x
            i = nexti
        return ret
                





    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
