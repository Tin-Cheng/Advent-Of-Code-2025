# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/9

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 9

    def fill_area(self, area: set[tuple[int, int]], start: tuple[int, int]) -> set[tuple[int, int]]:
        filled = area.copy()
        stack = [start]
        while stack:
            x, y = stack.pop()
            if (x, y) not in filled:
                filled.add((x, y))
                stack.append((x+1, y))
                stack.append((x-1, y))
                stack.append((x, y+1))
                stack.append((x, y-1))
        return filled

    @answer(4761736832)
    def part_1(self) -> int:
        pts = [tuple(map(int, line.split(","))) for line in self.input]
        max_retangle_area = 0
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                x1, y1 = pts[i]
                x2, y2 = pts[j]
                length = abs(x2 - x1) + 1
                width = abs(y2 - y1) + 1
                area = length * width
                if area > max_retangle_area:
                    max_retangle_area = area
        return max_retangle_area

    @answer(1452422268)
    # @wrong_answer(92348)
    def part_2(self) -> int:
        pts = [tuple(map(int, line.split(","))) for line in self.input]
        ori_x = [p[0] for p in pts]
        ori_y = [p[1] for p in pts]
        ori_x = list(set(ori_x))
        ori_y = list(set(ori_y))
        x = []
        y = []
        for v in ori_x:
            x.append(v)
            x.append(v + 1)
            x.append(v - 1)
        for v in ori_y:
            y.append(v)
            y.append(v + 1)
            y.append(v - 1)
        x = list(set(x))
        y = list(set(y))
        x.sort()
        y.sort()
        xmap = {}
        ymap = {}
        c_pts = []
        for p in pts:
            c_pts.append((x.index(p[0]), y.index(p[1])))
            xmap[x.index(p[0])] = p[0]
            ymap[y.index(p[1])] = p[1]

        area = set()
        for i in range(len(c_pts)):
            ni = (i + 1) % len(c_pts)
            x1, y1 = c_pts[i]
            x2, y2 = c_pts[ni]
            for xi in range(min(x1, x2), max(x1, x2)+1):
                for yi in range(min(y1, y2), max(y1, y2)+1):
                    area.add((xi, yi))

        startx, starty = [c_pts[0][0]+1, c_pts[0][1]+1]
        if not self.use_test_data:
            #observe from input
            startx, starty = 579, 378
        
        area_fill = self.fill_area(area, (startx, starty))

        max_rectangles = []
        for i in range(len(c_pts)):
            for j in range(i + 1, len(c_pts)):
                x1, y1 = c_pts[i]
                x2, y2 = c_pts[j]
                mapx1, mapy1 = xmap[x1], ymap[y1]
                mapx2, mapy2 = xmap[x2], ymap[y2]
                length = abs(mapx2 - mapx1) + 1
                width = abs(mapy2 - mapy1) + 1
                area = length * width
                max_rectangles.append((area, x1, y1, x2, y2,mapx1, mapy1, mapx2, mapy2))

        max_rectangles.sort()
        for area, x1, y1, x2, y2,mapx1, mapy1, mapx2, mapy2 in reversed(max_rectangles):
            can_fill = True
            for xi in range(min(x1, x2), max(x1, x2)+1):
                for yi in range(min(y1, y2), max(y1, y2)+1):
                    if (xi, yi) not in area_fill:
                        can_fill = False
                        break
                if not can_fill:
                    break
            if can_fill:
                return area
        return -1

        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
