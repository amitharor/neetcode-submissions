'''
Input(s): m x n grid (int)
Output: if element is 0, update it's entire row and col to 0, return updated matrix

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= (2^31) - 1 -> -2,147,483,648 to 2,147,483,647

Approach:
two passes

Time: O(m * n)
Space: O(1)
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

# firstRowHasZero

        firstRowHasZero = False
        for col in range(COLS):
            if matrix[0][col] == 0:
                firstRowHasZero = True


        firstColHasZero = False
        for row in range(ROWS):
            if matrix[row][0] == 0:
                firstColHasZero = True

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0 # marker; this row needs to be zeroing
                    matrix[0][col] = 0 # marker; this col needs to be zeroing

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0


        if firstRowHasZero:
            for col in range(COLS):
                matrix[0][col] = 0
        if firstColHasZero:
            for row in range(ROWS):
                matrix[row][0] = 0