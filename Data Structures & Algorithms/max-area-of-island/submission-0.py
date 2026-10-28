'''
Input(s): grid (int)
Output: return max area of an island in grid; return 0 if no island exists

Constraints:
1 <= grid.length, grid[i].length <= 50

Approach:
DFS

Time: O(m * n)
Space: O(m * n)
'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])


        def area(row, col):
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] != 1):
                return 0
            
            grid[row][col] = 0
            return (1 + area(row + 1, col) +
                    area(row - 1, col) +
                    area(row, col + 1) +
                    area(row, col - 1))

        largest = 0
        for row in range(ROWS):
            for col in range(COLS):
                largest = max(largest, area(row, col))
        
        return largest