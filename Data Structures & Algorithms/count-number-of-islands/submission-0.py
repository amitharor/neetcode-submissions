'''
Input(s): 2d grid (int)
Output: return num of islands

Constraints:
1 <= grid.length, grid[i].length <= 100
grid[i][j] is '0' or '1'.

Approach:
DFS

Time: O(m * n)
Space: O(m * n)
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def sink(row, col):
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] != '1'):
                return

            grid[row][col] = '0'
            sink(row + 1, col)
            sink(row - 1, col)
            sink(row, col + 1)
            sink(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    islands += 1
                    sink(row, col)

        return islands
        