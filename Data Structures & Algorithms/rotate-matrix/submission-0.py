'''
Input(s): n x n matrix (int)
Output: rotate matrix in place

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

Approach:
transpose matrix + reverse

Time: O(n^2)
Space: O(1)
'''


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # transpose
        for row in range(n):
            for col in range(row + 1, n): # above diagnol so we only swap once
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        # reverse
        for rowValues in matrix:
            rowValues.reverse()