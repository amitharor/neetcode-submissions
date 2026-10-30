'''
Input(s): 2d m * n matrix (int)
Output: return len of longest strictly increasing path within matrix

Constraints:
1 <= matrix.length, matrix[i].length <= 100

Approach:
dfs w memoization

Time: O(m * n) -> where m is num of rows and n is num of cols
Space: O(m * n)
'''


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        longestFrom = {} # (row, col) longest increasing path
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # down, up, right, left

        def dfs(row, col):
            if (row, col) in longestFrom:
                return longestFrom[(row, col)] # already computed -> reuse

            bestLen = 1 # cell by itself would be a path of 1
            for rowStep, colStep in directions:
                nextRow = row + rowStep
                nextCol = col + colStep
                inside = 0 <= nextRow < ROWS and 0 <= nextCol < COLS
                
                # only move to a bigger neighbor -> strictly increasing
                if inside and matrix[nextRow][nextCol] > matrix[row][col]:
                    bestLen = max(bestLen, 1 + dfs(nextRow, nextCol))

            longestFrom[(row, col)] = bestLen #save before returning
            return bestLen

        longestOverall = 0
        for row in range(ROWS):
            for col in range(COLS):
                longestOverall = max(longestOverall, dfs(row, col)) # path can start anywhere

        return longestOverall