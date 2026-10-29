'''
Input(s): m * n grid (int)
Output: return possible unique paths that can be taken from the top-left corner of grid to the bottom right corner.

Constraints:
1 <= m, n <= 100

Approach:
2D DP

Time: O(m * n)
Space: O(m * n)
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                fromAbove = paths[row - 1][col]
                fromLeft = paths[row][col - 1]
                paths[row][col] = fromAbove + fromLeft

        return paths[m - 1][n - 1] # bottom right cell