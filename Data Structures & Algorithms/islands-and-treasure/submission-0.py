'''
Input(s): m * n 2D grid
Output: fill each land cell with distance to its nearest treasure chest

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}


Approach:
BFS - queue

Time: O(m * n)
Space: O(m * n)
'''

from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()

        def addCell(row, col):
            if (min(row, col) < 0 or 
                    row == ROWS or 
                    col == COLS or 
                    (row, col) in visit or 
                    grid[row][col] == -1):
                return
            
            visit.add((row, col))
            queue.append([row, col])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append([row, col])
                    visit.add((row, col))

        
        distance = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = distance
                addCell(row + 1, col)
                addCell(row - 1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)

            distance += 1