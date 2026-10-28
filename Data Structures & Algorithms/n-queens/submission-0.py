'''
Input(s): n queens on n x n grid
Output: return all distinct solutions

Constraints:
1 <= n <= 8

Approach:
backtracking - hash set

Time: O(n!)
Space: O(n^2)
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        COLS = set()
        posDiag = set()
        negDiag = set()
        board = [['.'] * n for _ in range(n)]
        result = []

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return


            for col in range(n):
                if col in COLS or (row + col) in posDiag or (row - col) in negDiag:
                    continue
                
                COLS.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                COLS.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                board[row][col] = '.'

        backtrack(0)
        return result