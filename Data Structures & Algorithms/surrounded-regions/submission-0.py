'''
Input(s): m x n matrix board containing letters 'x' and 'o'
Output: capture regions that are surrounded.

Constraints:
1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.

Approach:
dfs

Time: O(m * n)
Space: O(m * n)
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def markSafe(row, col):
            if (row < 0 or
                col < 0 or
                row >= ROWS or
                col >= COLS or
                board[row][col] != 'O'):
                return

            board[row][col] = 'T' #temporarily safe
            markSafe(row + 1, col)
            markSafe(row - 1, col)
            markSafe(row, col + 1)
            markSafe(row, col - 1)
        
        for row in range(ROWS): #left and right edges
            markSafe(row, 0)
            markSafe(row, COLS - 1)

        for col in range(COLS): #top and bottom edges
            markSafe(0, col)
            markSafe(ROWS - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O':
                    board[row][col] = 'X' # Surrounded: capture
                elif board[row][col] == 'T':
                    board[row][col] = 'O' # Safe: restore




