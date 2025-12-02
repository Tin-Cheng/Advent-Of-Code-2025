# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 2

    def isSillyPattern(self, number: str) -> bool:
        if len(number) % 2:
            return False
        for i in range(len(number) // 2):
            if number[i] != number[i + len(number) // 2]:
                return False
        return True
    
    def isSillyPatternP2(self, number: str) -> bool:
        for i in range(len(number) // 2):
            pattern = number[0:i+1]
            if pattern * (len(number) // len(pattern)) == number:
                return True
        return False

    @answer(44854383294)
    def part_1(self) -> int:
        ret = 0
        for line in self.input[0].split(','):
            (frm, to) = line.split('-')
            for number in range(int(frm), int(to) + 1):
                if self.isSillyPattern(str(number)):
                    ret += int(number)
        return ret


    @answer(55647141923)
    def part_2(self) -> int:
        ret = 0
        for line in self.input[0].split(','):
            (frm, to) = line.split('-')
            for number in range(int(frm), int(to) + 1):
                if self.isSillyPatternP2(str(number)):
                    ret += int(number)
        return ret

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

