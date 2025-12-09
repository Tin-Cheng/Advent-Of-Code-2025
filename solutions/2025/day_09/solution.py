# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/9

from ...base import StrSplitSolution, answer
from typing import Set, Tuple, List, Dict
import itertools


class Solution(StrSplitSolution):
    """Day 9 solution (refactored for clarity).

    The input is a list of points as `"x,y"`. Part 1 finds the largest
    axis-aligned rectangle area determined by any two input points (inclusive
    coordinates). Part 2 reconstructs a coarse grid around the points,
    computes a filled region from a start point, and finds the largest
    rectangle (aligned to the coarse grid) that is fully inside the filled
    region.
    """

    _year = 2025
    _day = 9

    def flood_fill(self, blocked: Set[Tuple[int, int]], start: Tuple[int, int]) -> Set[Tuple[int, int]]:
        """Return the union of blocked cells and the connected region reachable
        from `start` (4-directional). The result is a set containing the
        blocked cells and any cells reached from `start` that were not
        originally blocked.
        """
        filled = set(blocked)
        stack = [start]
        while stack:
            x, y = stack.pop()
            if (x, y) in filled:
                continue
            filled.add((x, y))
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))
        return filled

    @answer(4761736832)
    def part_1(self) -> int:
        """Compute the largest axis-aligned rectangle area (inclusive) from any
        pair of input points.
        """
        points: List[Tuple[int, int]] = [tuple(map(int, line.split(","))) for line in self.input]
        max_area = 0
        for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
            length = abs(x2 - x1) + 1
            width = abs(y2 - y1) + 1
            max_area = max(max_area, length * width)
        return max_area

    @answer(1452422268)
    # @wrong_answer(92348)
    def part_2(self) -> int:
        """Rebuild a small integer grid around input points (including
        neighbors), mark the rectangles along polygon edges as blocked, flood
        fill from a start cell, and choose the largest rectangle (by real
        coordinate area) whose index-aligned cells are fully within the
        filled region.
        """
        points: List[Tuple[int, int]] = [tuple(map(int, line.split(","))) for line in self.input]

        def expand_coords(values: Set[int]) -> List[int]:
            expanded = set()
            for v in values:
                expanded.update((v - 1, v, v + 1))
            return sorted(expanded)

        xs = expand_coords({x for x, _ in points})
        ys = expand_coords({y for _, y in points})

        x_index: Dict[int, int] = {v: i for i, v in enumerate(xs)}
        y_index: Dict[int, int] = {v: i for i, v in enumerate(ys)}

        # coarse grid coordinates of input points
        coarse_points = [(x_index[x], y_index[y]) for x, y in points]

        # blocked cells are rectangles between consecutive polygon points
        blocked: Set[Tuple[int, int]] = set()
        n = len(coarse_points)
        for i in range(n):
            x1, y1 = coarse_points[i]
            x2, y2 = coarse_points[(i + 1) % n]
            for xi in range(min(x1, x2), max(x1, x2) + 1):
                for yi in range(min(y1, y2), max(y1, y2) + 1):
                    blocked.add((xi, yi))

        # choose a start inside the region; keep original behaviour for real input
        start = (coarse_points[0][0] + 1, coarse_points[0][1] + 1)
        if not self.use_test_data:
            # observed starting point for the real input
            start = (579, 378)

        filled = self.flood_fill(blocked, start)

        # consider all pairs of coarse points as candidate rectangle corners
        candidates = []
        for (i1, j1), (i2, j2) in itertools.combinations(coarse_points, 2):
            mapx1, mapy1 = xs[i1], ys[j1]
            mapx2, mapy2 = xs[i2], ys[j2]
            real_area = (abs(mapx2 - mapx1) + 1) * (abs(mapy2 - mapy1) + 1)
            candidates.append((real_area, i1, j1, i2, j2))

        # sort descending by real_area so we can return first valid largest
        candidates.sort(reverse=True)

        for real_area, i1, j1, i2, j2 in candidates:
            ok = True
            for xi in range(min(i1, i2), max(i1, i2) + 1):
                for yi in range(min(j1, j2), max(j1, j2) + 1):
                    if (xi, yi) not in filled:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                return real_area

        return -1

