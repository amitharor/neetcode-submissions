'''
Input(s): 2d matrix of distinct int
Output: return min amount of time it will take until it's possible te reach the bottom right sq

Constraints:
grid.length == grid[i].length
1 <= grid.length <= 50
0 <= grid[i][j] < n^2


Approach:
Dijkstra - min heap

Time: O(n^2 log n)
Space: O(n^2)
'''

import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)] # (highest cell on this path, row, col)
        visited = {(0,0)}
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]

        while heap:
            highest, row, col = heapq.heappop(heap) # the path with the lowest "tallest cell"
            if row == n - 1 and col == n -1:
                return highest # first arrival is best

            for rowStep, colStep in directions:
                newRow, newCol = row + rowStep, col + colStep

                if (
                    0 <= newRow < n and
                    0 <= newCol < n and
                    (newRow, newCol) not in visited
                    ):
                    visited.add((newRow, newCol))

                    newHighest = max(highest, grid[newRow][newCol])
                    heapq.heappush(heap, (newHighest, newRow, newCol))
                

