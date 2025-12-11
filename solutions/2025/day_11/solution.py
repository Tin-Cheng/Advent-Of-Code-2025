# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/11

from ...base import StrSplitSolution, answer
from collections import defaultdict

class Solution(StrSplitSolution):
    _year = 2025
    _day = 11

    @answer(753)
    def part_1(self) -> int:
        machines = []
        m = defaultdict(list)
        for line in self.input:
            name = line[:line.index(':')]
            machines.append(name)
        for line in self.input:
            items = line.split()
            frm = items[0][0:3]
            for i, item in enumerate(items):
                if i == 0:
                    continue
                m[frm].append(item)
        return self.searchGoal(m, {}, "you", "out")

    @answer(450854305019580)
    def part_2(self) -> int:
        machines = []
        m = defaultdict(list)
        for line in self.input:
            name = line[:line.index(':')]
            machines.append(name)
        for line in self.input:
            items = line.split()
            frm = items[0][0:3]
            for i, item in enumerate(items):
                if i == 0:
                    continue
                m[frm].append(item)
        scntf = self.searchGoal(m, {}, "svr", "fft")
        scntd = self.searchGoal(m, {}, "svr", "dac")
        dcnt = self.searchGoal(m, {}, "dac", "fft")
        fcnt = self.searchGoal(m, {}, "fft", "dac")
        ocntf = self.searchGoal(m, {}, "fft", "out")
        ocntd = self.searchGoal(m, {}, "dac", "out")
        return scntf * fcnt * ocntd + scntd * dcnt * ocntf

    def searchGoal(self, m, result, s, e):
        if (s+e) in result:
            return result[s+e]
        cnt = 0
        for next in m[s]:
            if next == e:
                cnt +=1
            else:
                cnt += self.searchGoal(m, result, next, e)
        result[s+e] = cnt
        return cnt

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
