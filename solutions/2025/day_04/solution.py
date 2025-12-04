# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/4

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 4

    def isAccessable(self, M, rows, cols, r, c, count):
        cnt = 0
        for dr, dc in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if M[nr][nc] == '@':
                    cnt += 1
                if cnt >= count:
                    return False
        return True
        
    @answer(1424)
    def part_1(self) -> int:
        ret = 0
        M = self.input
        rows, cols = len(M), len(M)
        for r in range(rows):
            for c in range(cols):
                if M[r][c] == '@':
                    ret += self.isAccessable(M, rows, cols, r, c, 4)
        return ret


    @answer(8727)
    def part_2(self) -> int:
        ret = 0
        M = self.input
        rows, cols = len(M), len(M)
        changed = True
        while changed:
            changed = False
            for r in range(rows):
                for c in range(cols):
                    if M[r][c] == '@':
                        if self.isAccessable(M, rows, cols, r, c, 4):
                            ret += 1
                            changed = True
                            M[r] = M[r][:c] + '.' + M[r][c+1:]
        return ret

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
