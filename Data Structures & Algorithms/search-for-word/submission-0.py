'''
Input(s): 2d grid (str), word (str)
Output: bool; return True if word found in grid; else False

Constraints:
1 <= board.length, board[i].length <= 5
1 <= word.length <= 10
board and word consists of only lowercase and uppercase English letters.


Approach:
backtracking

Time: O(m * 4^n)
Space: O(n)
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or 
                c < 0 or 
                r >= ROWS or 
                c >= COLS or 
                word[i] != board[r][c] or 
                board[r][c] == '#'):

                return False

            board[r][c] = '#'
            result = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return result

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False