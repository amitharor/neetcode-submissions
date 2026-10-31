'''
Input(s): m x n matrix (int)
Output: return list of all elements within the matric in spiral order

Constraints:
1 <= matrix.length, matrix[i].length <= 10
-100 <= matrix[i][j] <= 100

Approach:
count backwards with range (math)

Time: O(m * n) every cell is added once
Space: O(1)
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # top row -> left to right
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

        
            # right col -> top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1    

            # bottom row still left -> right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # left col -> bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][col])
                left += 1

        return result