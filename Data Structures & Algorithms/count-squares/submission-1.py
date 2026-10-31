'''
Input(s): stream (xy coord)
Output: implement CountSq class

Constraints:
point.length == 2
0 <= x, y <= 1000

Approach:
hash map of point counts and try each stored point as the diagonal corner

Time: O(1)
Space: O(n)
'''

from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.pointCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pointCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        queryX, queryY = point
        total = 0

        for (x, y), diagonalCount in self.pointCount.items():
            sideX = abs(queryX - x)
            sideY = abs(queryY - y)

            if sideX != sideY or sideX == 0:
                continue

            cornerA = self.pointCount.get((queryX, y), 0)
            cornerB = self.pointCount.get((x, queryY), 0)
            total += diagonalCount * cornerA * cornerB

        return total
