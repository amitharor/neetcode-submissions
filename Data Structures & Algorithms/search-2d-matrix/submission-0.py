'''
input: 2d array (int), target (int)
output: bool; return True if target exists within Matrix; else False

constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000


approach:
use binary search on the rows to narrow down to row with potential target num

return true if found; else false

time: O(log m*n)
space: O(1)

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        left, right = 0, (ROWS * COLS) - 1

        while left <= right:
            mid = (left + right) // 2
            r, c = mid // COLS, mid % COLS

            if matrix[r][c] < target:
                left = mid + 1
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                return True
        return False