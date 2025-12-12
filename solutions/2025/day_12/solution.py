# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/12

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 12

    def validatePossible(self, line: str, patternsCounts: list[int]) -> bool:
        size, quantities  = line.split(':')
        x, y = size.split('x')
        space = int(x) * int(y)
        areaNeeded = 0
        
        for i, quantity in enumerate(quantities.split()):
            areaNeeded += patternsCounts[i] * int(quantity)
        return areaNeeded <= space
    
    # @answer(1234)
    def part_1(self) -> int:
        patterns = []
        for i in range(6):
            pattern = []
            for j in range(3):
                pattern.append(self.input[i * 5 + j + 1])
            patterns.append(pattern)

        patternsCounts = []
        for pattern in patterns:
            count = 0
            for line in pattern:
                for c in line:
                    if c == '#':
                        count += 1
            patternsCounts.append(count)
        ret = 0
        for line in self.input[6 * 5:]:
            if self.validatePossible(line, patternsCounts):
                ret += 1

        return ret

            
        

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
