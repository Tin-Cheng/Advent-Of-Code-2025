# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/10

from ...base import StrSplitSolution, answer
import heapq
from z3 import *

class Solution(StrSplitSolution):
    _year = 2025
    _day = 10

    def parseInput(self, input) -> tuple[list[str], list[list[list[int]]], list[list[int]]]:
        goals = []
        buttonsSets = []
        P2goals = []
        for line in input:
            comp = line.split()
            goals.append(comp[0][1:-1])
            buttonsSets.append([list(map(int, c[1:-1].split(","))) for c in comp[1:-1]])
            P2goals.append(list(map(int, comp[-1][1:-1].split(","))))
        return (goals, buttonsSets, P2goals)

    def solveButtons(self, goal, buttonsSets):
        start = goal.replace('#','.')
        q = [(0, start, set())]
        cache = {}
        cache[start] = 0
        while q:
            (step, current, seen) = heapq.heappop(q)
            for i, buttons in enumerate(buttonsSets):
                next = current
                for button in buttons:
                    next = next[:button] + ('#' if next[button] == '.' else '.') + next[button + 1:]
                if next == goal:
                    return step + 1
                if next in cache:
                    continue
                cache[next] = step + 1
                nextSeen = seen.copy()
                nextSeen.add(i)
                heapq.heappush(q, (step + 1 , next, nextSeen))
        return -1

    """ def solveButtonsP2(self, goal, buttonsSet, current, index = 0, step = 0, currentMin = 99999):
        #print('solveButtonsP2', index, step, current)
        goalStr = str.join(',', map(str, goal))
        if index == len(buttonsSet):
            return 99999
        maxClick = 99999
        for button in buttonsSet[index]:
            maxClick = min(maxClick, goal[button] - current[button])

        for clicks in range(maxClick + 1, -1, -1):
            if clicks + step >= currentMin:
                continue
            next = current.copy()
            for button in buttonsSet[index]:
                next[button] += clicks
            nextStr = str.join(',', map(str, next))
            if nextStr == goalStr:
                currentMin = min(currentMin, step + clicks)
                return currentMin
            if index < len(buttonsSet) - 2 and len(buttonsSet[index]) > len(buttonsSet[index + 1]) and currentMin < 99999:
                return currentMin
            tryNextIndex = self.solveButtonsP2(goal, buttonsSet, next.copy(), index + 1, step + clicks)
            currentMin = min(currentMin, tryNextIndex)
        return currentMin """
    
    def solveP2Z3(self, goal, buttonsSet):
        newButtonsSet = []
        for buttons in buttonsSet:
            newButtons = [0] * len(goal)
            for b in buttons:
                newButtons[b] = 1
            newButtonsSet.append(newButtons)
        B = [ Int(f"b{i}") for i in range(len(newButtonsSet))]
        o = Optimize()
        for i in range(len(newButtonsSet)):
            o.add(B[i] >= 0)
        for i in range(len(goal)):
            o.add( Sum([ newButtonsSet[j][i] * B[j] for j in range(len(newButtonsSet))]) == goal[i])
        o.minimize( Sum(B))
        o.check()
        a = o.model()
        ret = 0
        for i in a:
            ret += a[i].as_long()
        return ret

        

    @answer(558)
    def part_1(self) -> int:
        (goals, buttonsSets, P2goals) = self.parseInput(self.input)
        ret = 0
        for i,(goal, buttons) in enumerate(zip(goals, buttonsSets)):
            ret += self.solveButtons(goal, buttons)
        return ret

    # @answer(1234)
    def part_2(self) -> int:
        (goals, buttonsSets, P2goals) = self.parseInput(self.input)
        ret = 0
        #ret += self.solveButtonsP2(P2goals[0], test, [0] * len(P2goals[0]))
        for i, (goal, buttons) in enumerate(zip(P2goals, buttonsSets)):
            r = self.solveP2Z3(goal, buttons)
            ret += r
        return ret

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
