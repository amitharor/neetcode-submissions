'''
Input(s): 2d matrix grid
Output: return the min num of minutres that must pass until there are zero fresh fruites remain. if impossible, return -1

Constraints:
1 <= grid.length, grid[i].length <= 10


Approach:
bfs

Time: O(m * n) where m is the num of rows and n is the num of cols in grid
Space: O(m * n)
'''

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        time = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and queue:
            length = len(queue)

            for i in range(length):
                row, col = queue.popleft()

                for dirRow, dirCol in directions:
                    newRow, newCol = row + dirRow, col + dirCol

                    if (newRow in range(ROWS) and
                        newCol in range(COLS) and
                        grid[newRow][newCol] == 1
                        ):
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1